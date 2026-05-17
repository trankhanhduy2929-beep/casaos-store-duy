# Personal Timesheet (Image-ready)

Ứng dụng chấm công cá nhân chạy trên CasaOS theo mô hình cài trực tiếp từ image.

## Mô hình mới (Hướng 2)
- Dùng image: `ghcr.io/trankhanhduy2929-beep/personal-timesheet:latest`
- Không mount source code vào `/app`
- Chỉ mount dữ liệu:
  - `/DATA/AppData/personal_timesheet/data` -> `/app/data`

## Cổng truy cập
- `5555`
- URL: `http://IP-CASAOS:5555`

## ENV cần cấu hình
- `JWT_SECRET`
- `ADMIN_USERNAME`
- `ADMIN_PASSWORD`
- `ADMIN_FULL_NAME`
- `ALLOW_ADMIN_VIEW_PASSWORDS`

## Khuyến nghị bảo mật
- Đổi mật khẩu admin mạnh
- Dùng JWT secret dài và ngẫu nhiên
- Chỉ bật `ALLOW_ADMIN_VIEW_PASSWORDS=true` khi cần
