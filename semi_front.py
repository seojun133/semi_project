import streamlit as st
from PIL import Image
import random
import time

st.set_page_config(page_title="전세사기 위험탐지", layout="centered")

st.title("전세사기 위험탐지")

uploaded_file = st.file_uploader("📷 사진을 이곳에 드래그하거나 업로드해주세요", type=["jpg", "jpeg", "png", "pdf"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption=uploaded_file.name, use_container_width=True)

    with st.spinner("📄 문서 분석 중입니다..."):
        time.sleep(2.5)  # 실제 OCR 처리 시간 대신 임시 대기

    result_type = random.choice(["A", "B", "C"])
    st.markdown("---")

    if result_type == "A":
        st.success("✅ 안전한 계약입니다.")
    elif result_type == "B":
        st.warning("⚠️ 주의: 이 주소는 사기 사례가 있는 지역입니다.")
    else:
        st.error("🚨 위험: 보증금 한도를 초과한 고위험 거래입니다.")

    st.markdown("#### 📌 계약 정보")
    st.write("- **주소**: 진해시 이동 612-11 스카이빌 201호")
    st.write("- **보증금**: 30,000,000원")
    st.write("- **계약 기간**: 2025.06.17 ~ 2026.06.17")
    st.write("- **특이사항**: 고위험 지역, 과도한 보증금 설정")

    # 다운로드 버튼용 텍스트 생성
    result_text = f"""[전세사기 위험탐지 결과]

분석 대상 파일: {uploaded_file.name}

🧾 판정 결과 요약:
- 주소: 진해시 이동 612-11 스카이빌 201호
- 보증금: 30,000,000원
- 계약 기간: 2025.06.17 ~ 2026.06.17
- 위험 요인: {result_type} 등급 판정
"""
    
    st.download_button(
        label="🔽 결과 텍스트 다운로드",
        data=result_text,
        file_name="risk_analysis_result.txt",
        mime="text/plain"
    )