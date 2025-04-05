import streamlit as st
from parser.pdf_parser import extract_info
from utils.calculator import generate_simulation_data
from utils.pdf_generator import create_pdf_report

st.set_page_config(page_title="대출 리포트 자동 생성기", layout="centered")
st.title("📄 대출 리포트 자동 생성기")

pdf_file = st.file_uploader("1️⃣ 등기부등본 PDF 업로드", type=["pdf"])
kb_price = st.number_input("2️⃣ KB 시세 입력 (단위: 만원)", step=1000, format="%d")

if pdf_file and kb_price:
    with st.spinner("🔍 리포트를 생성 중입니다..."):
        info = extract_info(pdf_file, kb_price)
        sim_table = generate_simulation_data(kb_price)
        pdf_path = create_pdf_report(info, sim_table)

    with open(pdf_path, "rb") as f:
        st.success("✅ 리포트 생성 완료!")
        st.download_button("📥 PDF 리포트 다운로드", f, file_name="대출_리포트.pdf")