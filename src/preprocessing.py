import pandas as pd
import os
from .dataset import setup_data, TARGET_DIR

def load_data():
    """
    Đảm bảo tập dữ liệu đã được tải xuống và tải tệp insurance.csv.
    """
    setup_data()
    file_path = os.path.join(TARGET_DIR, "insurance.csv")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Không tìm thấy tệp dữ liệu tại {file_path}")
    
    return pd.read_csv(file_path)

def remove_outliers_iqr(df, column):
    """
    Loại bỏ các giá trị ngoại lệ từ một cột cụ thể bằng phương pháp Khoảng tứ phân vị (IQR).
    """
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    filtered_df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    
    print(f"Đã loại bỏ {len(df) - len(filtered_df)} giá trị ngoại lệ từ cột '{column}' bằng phương pháp IQR.")
    return filtered_df
