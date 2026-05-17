# GitHub Release Guard (Image-ready)

Upload, scan và publish GitHub Release từ CasaOS theo kiểu **cài phát chạy luôn**.

## Mô hình mới (Hướng 2)
- CasaOS chạy trực tiếp image: `ghcr.io/trankhanhduy2929-beep/github-release-guard:latest`
- Không cần mount source code vào `/app`
- Chỉ cần mount dữ liệu runtime:
  - `/DATA/AppData/github-release-guard/uploads` -> `/app/uploads`
  - `/DATA/AppData/github-release-guard/data` -> `/app/data`

## ENV bắt buộc
- `GITHUB_TOKEN`: token GitHub có quyền repo cần thao tác
- `DEFAULT_OWNER`: owner mặc định
- `APP_PASSWORD`: mật khẩu đăng nhập web app lần đầu
- `SESSION_SECRET`: chuỗi bí mật dài (>=32 ký tự)

## Port mặc định
- `5566`

## Build image (repo source)
Source app ở thư mục `github-release-guard-app` đã có workflow GHCR:
- `.github/workflows/docker-publish.yml`

Khi push `main`, workflow sẽ build/push:
- `ghcr.io/<owner>/github-release-guard:latest`
- và tag theo release/tag nếu có
