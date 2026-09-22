import streamlit as st
import google.generativeai as genai

st.title("Ứng dụng AI của riêng tôi 🤖")

# Lấy chìa khóa API từ két sắt
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# BẮT BUỘC PHẢI CÓ CHỮ "models/" Ở TRƯỚC
model = genai.GenerativeModel('models/gemini-2.5-flash')

user_input = st.text_input("Bạn muốn hỏi gì?")

if st.button("Gửi"):
    if user_input:
        with st.spinner('Đang suy nghĩ...'):
            try:
                response = model.generate_content(user_input)
                st.write(response.text)
            except Exception as e:
                # Dòng này giúp in thẳng lỗi ra màn hình nếu vẫn còn trục trặc, không bị giấu đi nữa
                st.error(f"Hệ thống báo lỗi: {e}")
    else:
        st.warning("Vui lòng nhập câu hỏi của bạn!")
