# Y Đức Booking V2 (Image-ready)

Web booking cho **Phòng khám đa khoa Y Đức Sài Gòn** chạy theo mô hình image-based, cài trực tiếp từ CasaOS custom store.

## Mô hình mới (Hướng 2)
- Dùng image: `ghcr.io/trankhanhduy2929-beep/yduc-booking-v2:latest`
- Không mount source code vào `/app`
- Chỉ mount dữ liệu:
  - `/DATA/AppData/yduc-booking-v2/data` -> `/app/data`

## Cổng truy cập
- `3008`
- URL form đặt lịch: `http://IP-CASAOS:3008`
- URL admin: `http://IP-CASAOS:3008/admin/bookings`

## ENV cần cấu hình
- `PORT=3000`
- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_CHAT_ID`
- `ZALO_WEBHOOK_URL`
- `ZALO_WEBHOOK_SECRET`

## Tính năng
- Khách gửi form đặt lịch khám
- Lưu dữ liệu SQLite bền vững
- Gửi Telegram khi có booking mới
- Gửi webhook Zalo tùy chọn
- Admin xem danh sách đặt lịch
