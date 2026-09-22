import streamlit as st
import google.generativeai as genai

st.title("Ứng dụng AI của riêng tôi 🤖")

# Lấy chìa khóa API từ két sắt
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# SỬ DỤNG MODEL MỚI NHẤT TRONG DANH SÁCH CỦA BẠN
model = genai.GenerativeModel('gemini-2.5-flash')

# Khung nhập câu hỏi
user_input = st.text_input("Bạn muốn hỏi gì?")

if st.button("Gửi"):
    if user_input:
        with st.spinner('Đang suy nghĩ...'):
            response = model.generate_content(user_input)
            st.write(response.text)
    else:
        st.warning("Vui lòng nhập câu hỏi của bạn!")
