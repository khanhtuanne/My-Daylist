import streamlit as st
import google.generativeai as genai

st.title("Trang Kiểm Tra Lỗi 🔍")

# 1. Kiểm tra xem Streamlit có thấy API Key không
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    st.success(f"✅ Đã tìm thấy API Key trong két sắt (Độ dài: {len(api_key)} ký tự)")
    genai.configure(api_key=api_key)
except KeyError:
    st.error("❌ LỖI: Streamlit không tìm thấy GEMINI_API_KEY. Két sắt đang trống hoặc sai tên biến.")
    st.stop()

# 2. Kiểm tra xem API Key này được phép dùng những con AI nào của Google
st.write("Đang kết nối với Google để lấy danh sách model...")
try:
    models = list(genai.list_models())
    st.success("✅ Kết nối Google thành công!")
    st.write("Danh sách model bạn được phép dùng:")
    for m in models:
         if 'generateContent' in m.supported_generation_methods:
             st.code(m.name)
except Exception as e:
    st.error(f"❌ LỖI KẾT NỐI GOOGLE: {e}")
