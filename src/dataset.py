import kaggle
import os

# Mã định danh tập dữ liệu trên Kaggle (owner/dataset-name)
DATASET_NAME = "mirichoi0218/insurance"

# Thư mục cục bộ nơi lưu trữ các tệp CSV của tập dữ liệu
TARGET_DIR = "./dataset"

def setup_data():
    # Tạo thư mục tập dữ liệu nếu nó chưa tồn tại
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)
        print(f"Đã tạo thư mục {TARGET_DIR}")

    # Kiểm tra xem các tệp CSV đã có sẵn chưa (nếu có thì bỏ qua bước tải)
    files_in_dir = os.listdir(TARGET_DIR)
    if not any(f.endswith('.csv') for f in files_in_dir):
        print(f"Đang tải tập dữ liệu về '{TARGET_DIR}'...")
        try:
            # Tải xuống và tự động giải nén tập dữ liệu
            kaggle.api.dataset_download_files(
                DATASET_NAME, path=TARGET_DIR, unzip=True
            )
            print("Tải xuống hoàn tất thành công!")
        except Exception as e:
            print(f"Đã xảy ra lỗi khi đang tải xuống: {e}")
    else:
        print("Dữ liệu đã có sẵn trong thư mục 'dataset'.")