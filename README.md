# VENDIX AI - Autonomous Vendor Risk & Compliance Governance Agent

> Built for **Anna AI OS - Founding Builder Challenge 2026**

Enterprise-grade autonomous AI agent that prevents risky vendor onboarding BEFORE contract signature. Evaluates vendors across 12 compliance policies and enforces human-in-the-loop governance.

### 🚀 Live Demo

**Live Web:** https://vendix-ai.onrender.com/
**Anna App Store:** `anna.partners/@sraveena1992/vendix-ai`

### 🎯 Signature Demo Scenario: The $120k Risky Cloud Vendor
**Vendor:** Apex Cloud Analytics | $120k Contract | Net 60 Terms | SOC2 Missing | Data Residency FAIL
1. Intake → 2. AI Reasoning (Score 82/100 HIGH) → 3. PENDING_APPROVAL → 4. Human Override → 5. SHA256 Audit Hash

### 🧠 12-Policy Engine
- RULE_001: ISO27001 Required
- RULE_002/011: SOC2 Type II Mandatory + Validity 12M
- RULE_003: Net 45 Payment Limit
- RULE_004: Data Residency EU/US
- RULE_005: Revenue > $500k
- RULE_006: Encryption at Rest AES-256
- RULE_007: Subprocessor Approval
- RULE_008: Insurance $1M+
- RULE_009: No Open CVE HIGH
- RULE_010: Sanction List Check
- RULE_012: DPA Signed

### ✨ Key Features - High Utility & Retention
- **Multiple Workflows:** Cloud / SaaS / Logistics Vendors
- **Human Approval Console:** Human Override Required for Score >=40
- **Tamper-Proof Audit:** SHA256 Hash + Timestamp + Blockchain Anchor (Simulated)
- **Analytics Telemetry:** Latency, Rules Evaluated, Confidence 92%, Compliance %
- **Polished UI:** 3-Panel Enterprise Dashboard (Intake | Risk Reasoning | Approval)

### 🔍 Transparent Claims
**REAL:** Deterministic scoring, SHA256 audit, PENDING_APPROVAL gate, measurable latency
**PROTOTYPE (Simulated):** Blockchain anchor display, D&B revenue API, IP geolocation - V2 roadmap

### 📦 Anna App Structure
- anna.json -> App Manifest, primary_function: run_governance_pipeline
- main.py -> 12-rules engine, VendixAIAgent class
- frontend/index.html -> Enterprise UI
- requirements.txt -> Pure Python

### 🧪 Measurable Tests
- 5 LOW risk -> AUTO_CLEARED
- 10 MEDIUM -> PENDING_APPROVAL  
- 5 HIGH like Apex -> PENDING + Override Required
- All return VERIFIED_VALID + audit hash

### 👩‍💻 Builder
Raveena Sharma | Lyallpur Khalsa College | Anna Founding Builder

### License
MIT
