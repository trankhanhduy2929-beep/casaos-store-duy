# Shop Admin (Image-ready)

Web quản lý sản phẩm/shop cho CasaOS theo mô hình cài đặt trực tiếp từ image.

## Mô hình mới (Hướng 2)
- Dùng image: `ghcr.io/trankhanhduy2929-beep/shop-admin:latest`
- Không cần mount source code vào `/app`
- Chỉ mount:
  - `/DATA/AppData/shop-admin/data` -> `/app/data`
  - `/DATA/AppData/shop-admin/uploads` -> `/app/uploads`

## Cổng truy cập
- `1235`
- URL: `http://IP-CASAOS:1235`

## ENV cần cấu hình
- `ADMIN_USERNAME`
- `ADMIN_PASSWORD`
- `SESSION_SECRET`

## Gợi ý
- Đổi mật khẩu admin mạnh
- Dùng session secret dài, ngẫu nhiên
