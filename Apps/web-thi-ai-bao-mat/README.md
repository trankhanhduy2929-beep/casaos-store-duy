# Web Thi AI Bảo Mật (Image-ready)

Ứng dụng web thi AI bảo mật đã chuyển sang mô hình image-based để cài trực tiếp từ CasaOS custom store.

## Mô hình mới (Hướng 2)
- Dùng image: `ghcr.io/trankhanhduy2929-beep/web-thi-ai-bao-mat:latest`
- Không mount source code vào `/app`
- Chỉ mount dữ liệu:
  - `/DATA/AppData/web-thi-ai-bao-mat/data` -> `/app/data`

## Cổng truy cập
- `1234`
- URL: `http://IP-CASAOS:1234`

## ENV cần cấu hình
- `PORT=80`
- `GROQ_API_KEY`
- `DOS_API_KEY`

## API kiểm tra nhanh
- `GET /api/health`
