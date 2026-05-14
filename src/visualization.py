import seaborn as sns
import matplotlib.pyplot as plt

def plot_age_vs_charges(df):
    """
    Biểu đồ phân tán (Scatter plot) giữa Tuổi và Chi phí, phân loại theo trạng thái hút thuốc.
    """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='age', y='charges', hue='smoker', palette='viridis', alpha=0.7)
    plt.title('Chi phí y tế vs Tuổi (theo trạng thái hút thuốc)')
    plt.xlabel('Tuổi')
    plt.ylabel('Chi phí')
    plt.show()

def plot_smoker_costs_boxplot(df):
    """
    Biểu đồ hộp (Boxplot) thể hiện sự phân bổ chi phí giữa người hút thuốc và không hút thuốc.
    """
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=df, x='smoker', y='charges', palette='Set2')
    plt.title('Phân bổ chi phí y tế theo trạng thái hút thuốc')
    plt.xlabel('Hút thuốc')
    plt.ylabel('Chi phí')
    plt.show()

def plot_correlation_heatmap(df):
    """
    Bản đồ nhiệt (Heatmap) của ma trận tương quan.
    """
    plt.figure(figsize=(10, 8))
    corr = df.select_dtypes(include=['number']).corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title('Bản đồ nhiệt tương quan giữa các đặc trưng số')
    plt.show()

def plot_bmi_vs_charges(df):
    """
    Biểu đồ phân tán giữa BMI và Chi phí.
    """
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='bmi', y='charges', hue='smoker', palette='magma', alpha=0.7)
    plt.title('Chi phí y tế vs BMI (theo trạng thái hút thuốc)')
    plt.xlabel('BMI')
    plt.ylabel('Chi phí')
    plt.show()
