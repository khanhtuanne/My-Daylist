import streamlit as st
import google.generativeai as genai

st.title("Ứng dụng AI của riêng tôi 🤖")

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# ĐỔI SANG PHIÊN BẢN 3.6 THEO ĐÚNG YÊU CẦU CỦA GOOGLE
model = genai.GenerativeModel('models/gemini-3.6-flash')

user_input = st.text_input("Bạn muốn hỏi gì?")

if st.button("Gửi"):
    if user_input:
        with st.spinner('Đang suy nghĩ...'):
            try:
                response = model.generate_content(user_input)
                st.write(response.text)
            except Exception as e:
                st.error(f"Hệ thống báo lỗi: {e}")
    else:
        st.warning("Vui lòng nhập câu hỏi của bạn!")
