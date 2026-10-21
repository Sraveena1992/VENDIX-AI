from flask import Flask, request, jsonify, send_from_directory
from main import run_governance_pipeline, parse_contract_text
import os
import pypdf

app = Flask(__name__, static_folder='frontend')

@app.route('/')
def index():
    return send_from_directory('frontend', 'index.html')

@app.route('/api/run', methods=['POST'])
def run():
    data = request.get_json() or {}
    result = run_governance_pipeline(data)
    return jsonify(result)

@app.route('/api/upload-pdf', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "Empty filename"}), 400

    try:
        reader = pypdf.PdfReader(file)
        extracted_text = ""
        for page in reader.pages:
            extracted_text += page.extract_text() or ""
        
        parsed_data = parse_contract_text(extracted_text)
        governance_result = run_governance_pipeline({"raw_text": extracted_text, **parsed_data})
        
        return jsonify({
            "status": "SUCCESS",
            "parsed_contract": parsed_data,
            "governance_result": governance_result
        })
    except Exception as e:
        return jsonify({"error": f"PDF Parsing failed: {str(e)}"}), 500

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('frontend', path)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
