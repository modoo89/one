import fitz  # PyMuPDF
import re

def extract_info(pdf_file, kb_price):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = "\n".join([page.get_text() for page in doc])
    doc.close()

    owner = re.search(r"소유자\s+([가-힣㈜]+)", text)
    addr = re.search(r"\[집합건물\]\s+(.+?제\d+호)", text)
    area = re.search(r"전유부분.*?(\d+\.\d+)㎡", text)

    owner = owner.group(1) if owner else "추출 실패"
    addr = addr.group(1).strip() if addr else "추출 실패"
    area = area.group(1) + "㎡" if area else "추출 실패"

    return {
        "소유자": owner,
        "주소": addr,
        "면적": area,
        "KB시세": f"{kb_price:,}만원"
    }