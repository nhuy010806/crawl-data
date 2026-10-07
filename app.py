import streamlit as st
import json
import time

st.set_page_config(page_title="Scrapfly Web Scraper", page_icon="🕷️", layout="wide")

st.title("🕷️ Web Scraper App (Scrapfly)")
st.write("Giao diện cào dữ liệu sử dụng thư viện từ `scrapfly-scrapers`.")

# Sidebar để nhập API Key và cấu hình
with st.sidebar:
    st.header("⚙️ Cấu hình")
    api_key = st.text_input("🔑 Nhập Scrapfly API Key:", type="password", help="Bạn cần có API Key từ trang scrapfly.io để chạy.")
    
    # Cho phép người dùng chọn loại trang web muốn cào
    target_site = st.selectbox("🌐 Chọn trang web đích:", 
                               ["Booking.com", "Google Maps", "Facebook", "Instagram", "Khác..."])

# Khung nhập URL chính
url_input = st.text_input("🔗 Nhập URL bạn muốn cào dữ liệu:", "https://www.booking.com/hotel/vn/...")

# Nút chạy scraper
if st.button("🚀 Chạy Scraper", type="primary"):
    if not api_key:
        st.warning("⚠️ Vui lòng nhập Scrapfly API Key ở menu bên trái trước khi chạy!")
    elif not url_input.startswith("http"):
        st.warning("⚠️ Vui lòng nhập một URL hợp lệ bắt đầu bằng http:// hoặc https://")
    else:
        with st.spinner(f"Đang tiến hành lấy dữ liệu từ: {url_input}..."):
            # Ở đây bạn sẽ gọi script Python thật từ thư mục scrapfly-scrapers
            # Ví dụ: data = await scrape_booking_com(url, api_key)
            
            # --- CODE DEMO MÔ PHỎNG THỜI GIAN CHỜ ---
            time.sleep(2) 
            
            # Giả lập dữ liệu trả về sau khi cào
            mock_scraped_data = {
                "target": target_site,
                "url": url_input,
                "status": "success",
                "data": {
                    "name": "Khách sạn Golden Đà Nẵng",
                    "price": "1,200,000 VND",
                    "rating": 8.5,
                    "reviews": 120
                }
            }
            # ---------------------------------------
            
        st.success("✅ Cào dữ liệu thành công!")
        
        # Hiển thị dữ liệu lên màn hình
        st.subheader("📊 Kết quả:")
        st.json(mock_scraped_data)
        
        # Tạo chuỗi JSON để tải về
        json_string = json.dumps(mock_scraped_data, indent=4, ensure_ascii=False)
        
        # Nút TẢI VỀ
        st.download_button(
            label="⬇️ Tải dữ liệu về máy (.json)",
            data=json_string,
            file_name=f"scraped_data_{target_site.lower()}.json",
            mime="application/json"
        )
