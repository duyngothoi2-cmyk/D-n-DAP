# Hệ thống định giá bất động sản tự động dựa trên tin đăng CafeLand

Dự án của Nhóm 9 và Nhóm 13 cho học phần **Lập trình Phân tích Dữ liệu (4203014105)**.

## 1. Mục tiêu dự án

Dự án xây dựng mô hình hồi quy để dự đoán giá rao bán và giá cho thuê bất động sản dựa trên thuộc tính của tin đăng: diện tích, vị trí, số phòng, loại hình bất động sản và tình trạng pháp lý.

Biến mục tiêu chính được lựa chọn là **đơn giá trên mỗi m²**, đơn vị **triệu VNĐ/m²**, thay vì tổng giá. Đơn giá giúp so sánh các bất động sản có quy mô khác nhau và giảm ảnh hưởng trực tiếp của diện tích lên giá trị tổng. Phân phối và ngoại lai của đơn giá vẫn phải được kiểm tra trong bước tiền xử lý.

Mục tiêu kinh doanh là cung cấp mức giá tham chiếu để:

- Người bán hoặc người cho thuê định giá phù hợp.
- Người mua hoặc người thuê có cơ sở so sánh và thương lượng.
- Môi giới và nền tảng CafeLand hỗ trợ tư vấn khách hàng, đánh giá tin đăng và tối ưu hiệu quả niêm yết.
- Nhà đầu tư và doanh nghiệp có thêm cơ sở phân tích mặt bằng giá.

## 2. Câu hỏi nghiên cứu

### Câu hỏi chính

Các đặc điểm vật lý như diện tích, mặt tiền, số phòng và vị trí địa lý như quận/huyện, phường/xã ảnh hưởng như thế nào đến đơn giá rao bán nhà đất, và mô hình máy học nào cho độ chính xác dự báo cao nhất trên dữ liệu CafeLand?

### Câu hỏi phụ

1. Tình trạng pháp lý, đặc biệt Sổ hồng/Sổ đỏ so với các loại giấy tờ khác, tạo ra mức chênh lệch giá trị pháp lý bao nhiêu phần trăm trong từng phân khúc?
2. Đơn giá nhà đất thay đổi như thế nào từ khu vực lõi trung tâm ra các quận/huyện ngoại thành? Có sự phân tầng phân khúc rõ rệt giữa các khu vực hay không?

## 3. Phạm vi dự án

- **Không gian:** các khu vực có lượng tin đăng/giao dịch lớn tại Thành phố Hồ Chí Minh.
- **Loại hình:** căn hộ chung cư, nhà riêng/nhà phố và đất nền dự án.
- **Thời gian dữ liệu:** tin đăng còn hiệu lực từ tháng 01/2025 đến tháng 09/2026.
- **Phạm vi dự đoán:** giá rao bán/cho thuê được thể hiện trong tin đăng, không đại diện hoàn toàn cho giá giao dịch thực tế.

## 4. Nguồn dữ liệu

### Nguồn chính theo Project Charter V3

- Website: `https://nhadat.cafeland.vn/nha-dat-ban`
- Phương án kỹ thuật dự kiến: Requests, BeautifulSoup, phân trang `?page=N`, checkpoint và giới hạn tần suất request.
- Các trường khảo sát được: tiêu đề, giá rao, diện tích, thành phố, quận/huyện, phường/xã, đường, số phòng ngủ, số toilet, pháp lý, hướng nhà và ngày cập nhật.

### Nguồn dự phòng/bổ sung

- NhaTot/Chợ Tốt: endpoint JSON công khai, đang được dùng trong notebook hiện tại như nguồn dự phòng.
- Batdongsan.com.vn: đang tạm hoãn vì request tự động trả HTTP 403. Parser HTML offline được giữ lại nhưng không tự gửi request.
- Bộ dữ liệu mở/Kaggle, moso.vn và horea.org.vn: chỉ xem xét khi được phép sử dụng và cần ghi rõ nguồn, giấy phép, thời điểm tải và giới hạn so sánh với dữ liệu CafeLand.

### Trạng thái triển khai hiện tại

Notebook hiện tại mới triển khai crawler NhaTot và lưu checkpoint tại `data/raw/nhatot_raw.csv`. Dữ liệu này là **nguồn dự phòng**, chưa thay thế cho bộ dữ liệu chính CafeLand trong Project Charter V3. CafeLand cần được triển khai bổ sung bằng phương án truy cập hợp lệ trước khi thực hiện kết luận cuối cùng theo đúng đề tài.

## 5. Biến đầu vào dự kiến

- **Vị trí:** tỉnh/thành phố, quận/huyện, phường/xã, tên đường.
- **Vật lý:** diện tích, mặt tiền, độ rộng đường vào, số phòng ngủ, số toilet, số tầng.
- **Pháp lý và loại hình:** tình trạng pháp lý, loại hình bất động sản.
- **Tương tác và thời gian:** ngày đăng tin và lượng tương tác nếu dữ liệu cung cấp được.

## 6. Rủi ro dữ liệu

- Thiếu diện tích, số phòng, số tầng, pháp lý hoặc các trường khác.
- Giá, diện tích và đơn vị đo được trình bày không đồng nhất.
- Một bất động sản có thể xuất hiện trong nhiều tin đăng.
- Giá hoặc diện tích có thể là ngoại lai hoặc bị nhập sai.
- Giá rao không phản ánh hoàn toàn giá giao dịch thực tế.
- Tin đăng có thể hết hạn, bị xóa hoặc thay đổi sau thời điểm thu thập.
- Website có thể thay đổi HTML hoặc giới hạn truy cập.
- Mô hình chỉ đại diện cho các khu vực và loại hình có trong dữ liệu TP.HCM.

## 7. Quy trình thực hiện

Dự án bám theo pipeline của môn học:

1. **Ask & Acquire:** xác định vấn đề, biến mục tiêu, câu hỏi nghiên cứu và thu thập tin đăng.
2. **Clean & Explore:** chuẩn hóa giá, diện tích, đơn vị đo, loại hình và pháp lý; loại trùng; xử lý thiếu; lọc bán/thuê và lọc đúng phạm vi TP.HCM; xử lý outlier.
3. **Analyze & Model:** xây dựng và so sánh Linear Regression, Decision Tree, Random Forest hoặc XGBoost tùy khả năng dữ liệu và thư viện.
4. **Tell & Deliver:** đánh giá kết quả, xác định yếu tố ảnh hưởng, rút ra insight và đưa ra khuyến nghị.

Mô hình được đánh giá bằng tối thiểu hai chỉ số trong nhóm **RMSE, MAE và R²**.

## 8. Yêu cầu sản phẩm cuối

- Tối thiểu 5.000 dòng và tối thiểu 8 biến sau khi lọc hợp lệ.
- Dataset raw, dataset đã làm sạch và data dictionary.
- Notebook/script chạy lại được theo đúng thứ tự pipeline.
- EDA với ít nhất 8 biểu đồ chuyên nghiệp và diễn giải cho từng biểu đồ.
- Ít nhất 2 mô hình dự đoán, có so sánh và giải thích ưu/nhược điểm.
- Tối thiểu 2 chỉ số đánh giá mô hình.
- Insight và khuyến nghị trả lời được câu hỏi kinh doanh.
- Báo cáo, slide và README hướng dẫn tái lập kết quả.
- Ghi chú minh bạch các phần được AI hỗ trợ.

## 9. Cấu trúc repository

```text
.
├── data/
│   ├── external/       # Dữ liệu ngoài, chỉ dùng khi có nguồn hợp lệ
│   ├── processed/      # Dữ liệu sau làm sạch
│   └── raw/            # Dữ liệu thô và checkpoint
├── logs/               # Log tiến trình và request
├── notebooks/          # Notebook EDA, mô hình và báo cáo
├── source/
│   └── thu_thap_data_du_phong.ipynb
├── test/               # Kiểm tra helper/parser
└── README.md           # Mục tiêu và hướng dẫn dự án
```

## 10. Cài đặt và chạy notebook hiện tại

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Mở `source/thu_thap_data_du_phong.ipynb` và chạy theo hướng dẫn ở đầu notebook. Crawler hiện tại:

- Đọc checkpoint cũ, không xóa dữ liệu đã có.
- Phân trang NhaTot bằng tham số `o`.
- Bỏ qua tin trùng theo ID hoặc URL.
- Ghi checkpoint sau mỗi 150 dòng.
- Dừng khi gặp HTTP 403/429 và không retry vô hạn.
- Không tạo dữ liệu giả để đạt số dòng mục tiêu.

## 11. Nguyên tắc truy cập dữ liệu

Không sử dụng CAPTCHA, cookie phiên cá nhân, token cá nhân, proxy xoay vòng, giả mạo fingerprint hoặc kỹ thuật vượt cơ chế bảo vệ website. Nếu nguồn trả 403, cần API, file export hoặc quyền truy cập chính thức.

Không commit dữ liệu raw lớn, response HTML hoặc log riêng lên GitHub. Các file này đã được loại trong `.gitignore`; chỉ commit dữ liệu mẫu nhỏ hoặc hướng dẫn tải dữ liệu khi cần.

## 12. Thành viên và phân công V3

- Ngô Thời Duy: trưởng nhóm, trưởng pipeline dữ liệu, đề cương, biến mục tiêu và kiến trúc thu thập.
- Châu Triệu Vỹ: khảo sát kỹ thuật và thu thập nhóm biến vị trí/vật lý.
- Nguyễn Phú Cường: đánh giá chống thu thập tự động, nhóm biến pháp lý, loại hình, giá và ngày đăng, xử lý lỗi.
- Nguyễn Lý Thành Nhân: kiến trúc dữ liệu và lưu trữ CSV/JSON/Parquet.
- Hoàng Bảo Hân: chất lượng dữ liệu, data dictionary, thiếu, trùng và ngoại lai ban đầu.
- Thành viên 6: tài liệu, thuyết trình và quản lý mã nguồn/thư viện.

## 13. Đẩy repository lên GitHub

```powershell
git init
git branch -M main
git remote add origin https://github.com/duyngothoi2-cmyk/D-n-DAP.git
git add README.md requirements.txt .gitignore source data logs test
git commit -m "Update README from Project Charter V3"
git push -u origin main
```

Trước khi commit, kiểm tra `git status` và `git diff --cached --stat` để chắc rằng không có dữ liệu nhạy cảm hoặc file raw lớn bị đưa lên repository.
