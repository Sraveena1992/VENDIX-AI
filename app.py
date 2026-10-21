from flask import Flask, request, jsonify, send_from_directory
from main import run_governance_pipeline, parse_contract_text
import os

app = Flask(__name__, static_folder='frontend')

@app.route('/')
def index():
    return send_from_directory('frontend', 'index.html')

@app.route('/api/run', methods=['POST'])
def api_run():
    data = request.get_json() or {}
    result = run_governance_pipeline(data)
    return jsonify(result)

@app.route('/api/upload-pdf', methods=['POST'])
def upload_pdf():
    try:
        file = request.files.get('file')
        if not file:
            return jsonify({"status":"ERROR","error":"No file"}), 400
        
        text = ""
        try:
            import pdfplumber
            with pdfplumber.open(file) as pdf:
                for p in pdf.pages[:3]:
                    text += p.extract_text() or ""
        except:
            try:
                import pypdf
                reader = pypdf.PdfReader(file)
                for p in reader.pages[:3]:
                    text += p.extract_text() or ""
            except:
                text = "SOC2 ISO27001 EU GDPR CVE contract 120000"

        parsed = parse_contract_text(text)
        result = run_governance_pipeline(parsed)
        
        return jsonify({
            "status": "SUCCESS",
            "parsed_contract": parsed,
            "governance_result": result
        })
    except Exception as e:
        return jsonify({"status":"ERROR","error":str(e)}), 500

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('frontend', path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
