from modules.pdf_extractor import extract_text
from modules.pii_detector import detect_pii
from modules.blur_generator import blur_text
from modules.summarizer import generate_summary

pdf_path = "uploads/sample.pdf"

# Step 1: Extract text from PDF
text = extract_text(pdf_path)

# Step 2: Detect PII (names, address, phone, etc.)
pii = detect_pii(text)

# Step 3: Blur / mask PII
protected_text = blur_text(text, pii)

# Step 4: Generate summary from SAFE text
summary = generate_summary(protected_text)

# Output
print("\nPROTECTED TEXT:\n")
print(protected_text)

print("\nSUMMARY:\n")
print(summary)