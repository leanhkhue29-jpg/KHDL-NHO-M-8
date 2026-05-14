import pandas as pd
from scipy import stats

def get_correlations(df):
    """
    Trả về ma trận tương quan cho các đặc trưng số.
    """
    return df.select_dtypes(include=['number']).corr()

def test_smoker_hypothesis(df):
    """
    Thực hiện kiểm định T-test độc lập để so sánh chi phí y tế giữa người hút thuốc và người không hút thuốc.
    """
    smokers = df[df['smoker'] == 1]['charges']
    non_smokers = df[df['smoker'] == 0]['charges']
    
    t_stat, p_val = stats.ttest_ind(smokers, non_smokers)
    
    results = {
        't_statistic': t_stat,
        'p_value': p_val,
        'significant': p_val < 0.05,
        'smoker_mean': smokers.mean(),
        'non_smoker_mean': non_smokers.mean()
    }
    
    return results
