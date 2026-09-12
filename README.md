# Dự đoán giá nhà đất tại Thành phố Hồ Chí Minh

Case study của nhóm 7, 8 cho môn **Lập trình Phân tích Dữ liệu (2101681)**.

## 1. Mục tiêu dự án

Nhóm đóng vai bộ phận Data/Product của một nền tảng proptech giả định CafeLand. Dự án xây dựng mô hình ước tính giá bán nhà đất tại TP.HCM dựa trên đặc điểm của tin đăng như diện tích, vị trí và loại hình bất động sản.

Kết quả hướng tới một khoảng giá tham chiếu đáng tin cậy để:

- Người bán định giá hợp lý và tăng khả năng bán nhanh.
- Người mua có cơ sở thương lượng và tránh giá chào quá cao.
- Đội ngũ môi giới có công cụ tư vấn và tăng uy tín nền tảng.

## 2. Câu hỏi nghiên cứu

1. Những yếu tố nào trong một tin đăng ảnh hưởng đến mức giá tham chiếu của một tin đăng mới?
2. Sau khi kiểm soát diện tích và loại nhà, khu vực nào đang có giá tương đối cao hoặc thấp? Chênh lệch giá giữa các khu vực đến từ vị trí hay từ quy mô và loại hình nhà ở?

## 3. Phạm vi và dữ liệu

- **Địa lý:** Thành phố Hồ Chí Minh.
- **Thời điểm:** Dữ liệu tin đăng còn hiệu lực tại thời điểm thu thập ngày 31/08 và 01/09/2026.
- **Nguồn theo Project Charter:**
  - CafeLand.vn: nguồn chính cho bộ dữ liệu nhà đất bán.
  - Batdongsan.vn: nguồn bổ sung.
  - Chotot.com: nguồn bổ sung.
- **Mục tiêu dữ liệu:** tối thiểu 5.000 dòng và 8 biến sau khi lọc hợp lệ.

### Trạng thái triển khai hiện tại

Notebook hiện có đang chạy endpoint JSON công khai của **NhaTot/Chợ Tốt** và lưu checkpoint tại `data/raw/nhatot_raw.csv`. Phần Batdongsan.com.vn đang tạm hoãn vì request tự động trả HTTP 403; parser offline được giữ riêng để xử lý response HTML hợp lệ nếu có sau này.

Việc triển khai hiện tại chưa thay thế đầy đủ bộ dữ liệu và nguồn mục tiêu trong Project Charter. CafeLand.vn và batdongsan.vn cần được bổ sung bằng dữ liệu, quyền truy cập hoặc phương án thu thập hợp lệ trước khi kết luận cuối cùng của dự án.

## 4. Quy trình phân tích

Dự án bám theo pipeline của môn học:

1. **Ask & Acquire:** xác định vấn đề kinh doanh, câu hỏi nghiên cứu và thu thập dữ liệu tin đăng.
2. **Clean & Explore:** chuẩn hóa loại hình, xử lý thiếu, loại trùng, tách bán/thuê, lọc đúng TP.HCM và xử lý outlier giá/diện tích.
3. **Analyze & Model:** xây dựng và so sánh ít nhất 2 mô hình dự đoán giá.
4. **Tell & Deliver:** diễn giải kết quả, rút ra 5-7 insight, đưa ra khuyến nghị và hoàn thiện báo cáo/slide.

## 5. Yêu cầu sản phẩm cuối

- GitHub repository có code, notebook, dữ liệu hoặc hướng dẫn tải dữ liệu, báo cáo và README.
- Dataset raw và dataset đã làm sạch kèm mô tả nguồn, cách thu thập và cấu trúc biến.
- Notebook hoặc script chạy lại được theo đúng thứ tự pipeline.
- EDA với ít nhất 8 biểu đồ chuyên nghiệp và phần diễn giải.
- Ít nhất 2 mô hình dự đoán, được so sánh bằng ít nhất 2 chỉ số phù hợp như R², RMSE hoặc MAE.
- 5-7 insight có ý nghĩa thực tế và trả lời được câu hỏi kinh doanh.
- Ghi chú minh bạch các phần được AI hỗ trợ và bảo đảm thành viên giải thích được code.

## 6. Cấu trúc repository

```text
.
├── data/
│   ├── external/       # Dữ liệu bên ngoài, không commit mặc định
│   ├── processed/      # Dữ liệu sau làm sạch
│   └── raw/            # Dữ liệu thô và checkpoint
├── logs/               # Log tiến trình và request
├── notebooks/          # Notebook EDA, mô hình và báo cáo phân tích
├── source/
│   └── thu_thap_data_du_phong.ipynb
├── test/               # Kiểm tra helper/parser
└── tham_khao/          # Project Charter và tài liệu môn học
```

## 7. Cài đặt

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## 8. Chạy notebook hiện tại

Mở `source/thu_thap_data_du_phong.ipynb` và chạy theo thứ tự các cell được hướng dẫn ở phần đầu notebook. Notebook hiện tại sẽ:

- Đọc checkpoint cũ thay vì xóa dữ liệu đã thu thập.
- Phân trang NhaTot bằng tham số `o`.
- Bỏ qua listing trùng theo ID hoặc URL.
- Ghi checkpoint sau mỗi 150 dòng.
- Dừng khi gặp HTTP 403/429 và không retry vô hạn.
- Không tạo dữ liệu giả để đạt số dòng mục tiêu.

## 9. Dữ liệu và quyền truy cập

Không commit dữ liệu raw lớn, response HTML hoặc log riêng lên GitHub. Các file này đã được loại trong `.gitignore`; chỉ commit dữ liệu mẫu nhỏ hoặc hướng dẫn tải dữ liệu khi cần.

Không sử dụng CAPTCHA, cookie phiên cá nhân, token cá nhân, proxy xoay vòng, giả mạo fingerprint hoặc kỹ thuật vượt cơ chế bảo vệ website. Nếu nguồn dữ liệu trả 403, cần API, export hoặc quyền truy cập chính thức.

## 10. Thành viên và tiến độ theo Charter

- Nhóm trưởng: Nguyễn Thị Trâm.
- Thành viên: Trần Thị Ngọc Ánh, Nguyễn Bá Công, Hà Trọng Hữu Duy, Lê Anh Duy, Văn Tường Vy.
- Tuần 4: Project Charter, câu hỏi nghiên cứu và GitHub repository.
- Tuần 7: dữ liệu raw, làm sạch sơ bộ và EDA.
- Tuần 8: mô hình và đánh giá.
- Tuần 9: báo cáo, slide, README và kiểm tra cuối.

## 11. Khởi tạo và đẩy GitHub

```powershell
git init
git branch -M main
git remote add origin https://github.com/duyngothoi2-cmyk/D-n-DAP.git
git add README.md requirements.txt .gitignore source data logs test tham_khao
git commit -m "Document project charter and data pipeline"
git push -u origin main
```

Trước khi commit, kiểm tra `git status` và `git diff --cached --stat` để chắc rằng không có dữ liệu nhạy cảm hoặc file raw lớn bị đưa lên repository.
