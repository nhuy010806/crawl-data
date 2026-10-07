import streamlit as st

st.set_page_config(page_title="My Scraper App", page_icon="🕷️")

st.title("Chào mừng đến với Web Scraper App 🕷️")
st.write("Đây là trang web dùng Streamlit. Bạn có thể gọi các script cào dữ liệu từ thư mục `scrapfly-scrapers` ở đây.")

url_input = st.text_input("Nhập URL bạn muốn cào dữ liệu:", "https://example.com")

if st.button("Chạy Scraper"):
    st.info(f"Đang tiến hành lấy dữ liệu từ: {url_input}")
    # Chèn logic gọi file python cào dữ liệu vào đây
    st.success("Cào dữ liệu thành công (Demo)!")
