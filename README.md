# Duy CasaOS App Store

Kho cấu hình Docker Compose để add vào CasaOS.

## Link add vào CasaOS

Sau khi push repo này lên GitHub public `trankhanhduy2929-beep/casaos-store-duy`, dùng link:

```text
[https://raw.githubusercontent.com/trankhanhduy2929-beep/casaos-store-duy/main/AppStore.json](https://github.com/trankhanhduy2929-beep/casaos-store-duy/archive/refs/heads/main.zip
)
```

## Cấu trúc

```text
AppStore.json
Apps/
  github-release-guard/
  personal-timesheet/
  casaos-shop-admin/
  yduc-booking/
  hass-addon-repo-app/
```

## Cách cập nhật

1. Thêm app mới vào `Apps/<app-id>/`
2. Tạo `docker-compose.yml`, `app.json`, `icon.svg`
3. Thêm app vào `AppStore.json`
4. Push lên GitHub
5. Refresh App Store trong CasaOS

## Lưu ý bảo mật

Các biến như password/token trong compose đang để mẫu. Khi cài trong CasaOS, nhớ đổi lại ENV cho mạnh trước khi chạy.
