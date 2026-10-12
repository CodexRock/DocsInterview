from pypdf import PdfReader

files = [
    ("Ace Your Case II - Fifteen More Consulting Cases (WetFeet Insider Guide) (WetFeet) (z-library.sk, 1lib.sk, z-lib.sk).pdf", "_case_ace.txt"),
    ("Case in Point 11 Complete Case Interview Preparation (Cosentino, Marc Patrick) (z-library.sk, 1lib.sk, z-lib.sk) 2.pdf", "_case_cip.txt"),
]

for f, outname in files:
    out = []
    try:
        reader = PdfReader(f)
        out.append(f"PAGES: {len(reader.pages)}")
        for i, page in enumerate(reader.pages):
            out.append(f"\n--- page {i+1} ---")
            out.append(page.extract_text() or "")
    except Exception as e:
        out.append("ERROR: " + str(e))
    with open(outname, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))
    print("done", outname)
