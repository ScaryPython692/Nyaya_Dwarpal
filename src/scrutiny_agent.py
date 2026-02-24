import PyPDF2
import hashlib

# --- INGREDIENT 1: The Bhashini Translator (Mock) ---
def mock_bhashini_translate(text, target_lang="Hindi"):
    translations = {
        "Hindi": {
            "Missing Vakalatnama (Power of Attorney)": "वकालतनामा (मुख्तारनामा) गायब है",
            "Court Fee calculation not found": "कोर्ट फीस की गणना नहीं मिली",
            "Jurisdiction statement missing": "क्षेत्राधिकार का विवरण गायब है",
            "Digital Signature placeholder not detected": "डिजिटल हस्ताक्षर का स्थान नहीं मिला"
        }
    }
    return translations.get(target_lang, {}).get(text, f"[Translation Pending for {text}]")

# --- INGREDIENT 2: The Digital DNA Generator ---
def generate_digital_dna(pdf_path):
    sha256_hash = hashlib.sha256()
    with open(pdf_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

# --- INGREDIENT 3: The Text Reader ---
def extract_text_locally(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text
    except Exception as e:
        return f"Error reading file: {e}"

# --- INGREDIENT 4: The Scrutiny Logic ---
def run_gatekeeper_checks(extracted_text):
    findings = {"technical_defects": []}
    checks = {
        "Vakalatnama": "Missing Vakalatnama (Power of Attorney)",
        "Court Fee": "Court Fee calculation not found",
        "Jurisdiction": "Jurisdiction statement missing",
        "Signature": "Digital Signature placeholder not detected"
    }
    for keyword, error in checks.items():
        if keyword.lower() not in extracted_text.lower():
            findings["technical_defects"].append(error)
    return findings

# --- THE ACTUAL COOKING (Execution) ---
if __name__ == "__main__":
    # 1. SETUP: Make sure this file exists in your sidebar!
    test_pdf = "perfect_test.pdf" 
    
    # 2. DNA: Create the fingerprint
    dna = generate_digital_dna(test_pdf)
    print(f"🧬 Digital DNA (Hash): {dna}")
    
    # 3. SCRUTINY: Read the file
    print(f"🧐 NyayaDwarpal is scrutinizing: {test_pdf}...")
    content = extract_text_locally(test_pdf)
    results = run_gatekeeper_checks(content)

    # 4. OUTPUT: Show errors with Hindi translation
    if not results["technical_defects"]:
        print("✅ SUCCESS: Document is 'Hearing-Ready'!")
    else:
        print("\n❌ DEFECTS FOUND (Procedural Scrutiny):")
        for defect in results["technical_defects"]:
            hindi_msg = mock_bhashini_translate(defect, "Hindi")
            print(f"  - {defect}")
            print(f"    📢 (हिन्दी): {hindi_msg}")