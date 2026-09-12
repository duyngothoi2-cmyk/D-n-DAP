# Note tiến trình

| Thời gian | Lỗi phát sinh / Hướng sửa | Mô tả dễ hiểu |
|---|---|---|
| 2026-09-12 14:00 | NhaTot trả `403` khi cào HTML / Chuyển sang API JSON | Website chặn request HTML ngay từ trang đầu, nên dùng endpoint API thay cho đọc giao diện web. |
| 2026-09-12 14:10 | Tích hợp API NhaTot / Dùng `ads`, `offset`, checkpoint và parser 22 cột | Dữ liệu lấy trực tiếp từ JSON, ánh xạ vào các cột cần thiết và lưu từng đợt để có thể chạy tiếp. |
| 2026-09-12 14:15 | Batdongsan trả `403` tại `/p1` / Ghi log và chuẩn bị fail-fast | Batdongsan cũng chặn request tự động; crawler cũ thử tiếp nhiều trang rồi bị ngắt. |
| 2026-09-12 14:16 | Request bị `403/429` / Dừng ngay, giữ checkpoint và log | Không thử lặp vô ích; không né CAPTCHA, xoay IP hoặc giả mạo cơ chế bảo vệ. |
| 2026-09-12 14:20 | Batdongsan tiếp tục thử sau `403` / Sửa `crawl_batdongsan()` theo fail-fast | Gặp `403/429` thì dừng nguồn ngay, lưu checkpoint và không gửi thêm request; không thể đảm bảo website cho phép crawler nếu chưa có API/quyền chính thức. |

## Trạng thái hiện tại

- Notebook: `source/thu_thap_bat_dong_san_hcm.ipynb`
- File riêng: `data/raw/nhatot_raw.csv`, `data/raw/batdongsan_raw.csv`
- Dữ liệu thô, checkpoint mỗi 150 dòng, không gộp hai nguồn.
- Log chi tiết: `logs/request_blocked.log`
