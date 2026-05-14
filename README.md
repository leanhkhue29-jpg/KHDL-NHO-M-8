# 🏥 Dự án: Phân tích tập dữ liệu chi phí y tế cá nhân

Dự án này là một bài tập giữa kỳ tập trung vào việc khám phá và phân tích tập dữ liệu chi phí bảo hiểm y tế. Mục tiêu chính là xây dựng một khung **Kể chuyện bằng dữ liệu (Data Storytelling)** toàn diện để xác định các yếu tố chính ảnh hưởng đến chi phí y tế của một cá nhân.

---

## 👥 Thành viên nhóm

**Lớp:** Kinh tế Quốc tế CLC 66C - NEU
**Môn học:** Khoa học Dữ liệu
**Giảng viên:** TS. Trần Đức Minh

| Họ và tên | Mã sinh viên |
|---|---|
| Lê Anh Khuê | 11244315 |
| Phạm Thảo Linh | 11240277 |
| Nguyễn Ngọc Diệu Linh | 11241063 |
| Cao Mỹ Duyên | 11246852 |
| Phạm Xuân Bách | 11240018 |

---

## 📌 Tổng quan dự án

Dự án sử dụng tập dữ liệu từ Kaggle để phân tích mối tương quan giữa các đặc điểm nhân khẩu học và thói quen sinh hoạt (như tuổi tác, chỉ số BMI, tình trạng hút thuốc) đối với chi phí y tế. Từ đó, đưa ra các khuyến nghị thực tiễn cho việc định giá bảo hiểm và các chiến dịch sức khỏe cộng đồng.

**Các bước thực hiện chính:**
1. **Tiền xử lý dữ liệu:** Làm sạch, xử lý giá trị ngoại lệ (IQR) và mã hóa biến phân loại.
2. **Phân tích dữ liệu khám phá (EDA):** Kiểm chứng các giả thuyết và phân tích ma trận tương quan.
3. **Trực quan hóa:** Sử dụng Scatter Plot, Boxplot, Heatmap để làm nổi bật các phát hiện quan trọng.

---

## 📂 Cấu trúc kho lưu trữ

- `src/`: Mã nguồn Python xử lý dữ liệu (`preprocessing.py`, `analysis.py`, `visualization.py`, `dataset.py`).
- `dataset/`: Thư mục chứa dữ liệu thô (`insurance.csv`) sau khi tải về.
- `main.ipynb`: Jupyter Notebook triển khai quy trình phân tích hoàn chỉnh.
- `requirements.txt`: Danh sách các thư viện cần thiết.
- `CONTEXT.md`: Tài liệu ngữ cảnh dự án.

---

## ⚙️ Hướng dẫn thiết lập

### 1. Tạo môi trường ảo (Khuyên dùng)
Việc sử dụng môi trường ảo giúp quản lý các thư viện một cách độc lập và tránh xung đột hệ thống.

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Cài đặt thư viện
Sau khi đã kích hoạt môi trường ảo, chạy lệnh sau để cài đặt các thư viện cần thiết:

```bash
pip install -r requirements.txt
```

### 3. Thiết lập Kaggle API
Dự án này tự động tải dữ liệu từ Kaggle thông qua thư viện `kaggle`. Bạn cần thiết lập thông tin xác thực như sau:

1. Đăng nhập vào [Kaggle](https://www.kaggle.com/).
2. Truy cập vào **Account** -> Cuộn xuống phần **API** -> Chọn **Create New API Token**.
3. Một tệp `kaggle.json` sẽ được tải về máy tính của bạn. Nếu chưa có, hãy tự tạo và thêm `{'username':'<username>','key':'<key>'}` vào tệp `kaggle.json`.
4. Di chuyển tệp `kaggle.json` vào thư mục tương ứng trên hệ điều hành của bạn:
   - **Windows:** `C:\Users\<Tên_Người_Dùng>\.kaggle\kaggle.json`
   - **Linux/Mac:** `~/.kaggle/kaggle.json`
5. (Lưu ý: Nếu chưa có thư mục `.kaggle`, hãy tự tạo nó).

---

## 🚀 Cách chạy dự án

1. Mở tệp `main.ipynb` bằng Jupyter Notebook hoặc VS Code.
2. Chọn kernel Python phù hợp (đã cài đặt các thư viện ở bước trên).
3. Chạy tất cả các ô (*Run All*). 
   - Mã nguồn trong `src/dataset.py` sẽ tự động kiểm tra và tải dữ liệu từ Kaggle về thư mục `dataset/` nếu chưa có sẵn.

---

## 📊 Nguồn dữ liệu
[Kaggle - Medical Cost Personal Datasets](https://www.kaggle.com/datasets/mirichoi0218/insurance)
