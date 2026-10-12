import sys
from pypdf import PdfReader

files = [
    "Hamza_Archane_BCG2026CV.pdf",
    "Hamza_Archane_2026_Res.pdf",
    "Hamza_Archane_Google_FDE_Resume.pdf",
]

out = []
for f in files:
    out.append("=" * 80)
    out.append("FILE: " + f)
    out.append("=" * 80)
    try:
        reader = PdfReader(f)
        for i, page in enumerate(reader.pages):
            out.append(f"--- page {i+1} ---")
            out.append(page.extract_text() or "")
    except Exception as e:
        out.append("ERROR: " + str(e))
    out.append("")

with open("_resumes_text.txt", "w", encoding="utf-8") as fh:
    fh.write("\n".join(out))
print("done")
