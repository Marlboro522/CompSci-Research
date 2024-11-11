import pandas as pd
from scipy.stats import ttest_ind, ttest_rel

# Load the datasets
u10 = pd.read_csv('u10 (1).csv')
u25 = pd.read_csv('u25.csv')
u50 = pd.read_csv('u50.csv')

# Columns of interest
columns = ['S', 'I', 'P', 'IP', 'SI', 'SP', 'SIP', 'SwL', 'IwL', 'PwL']

# Perform independent t-tests
print("Independent T-Tests")
for col in columns:
    ttest_result_10_25 = ttest_ind(u10[col], u25[col], equal_var=False)
    ttest_result_25_50 = ttest_ind(u25[col], u50[col], equal_var=False)
    ttest_result_10_50 = ttest_ind(u10[col], u50[col], equal_var=False)
    
    print(f"{col} (u10 vs u25): Statistic={ttest_result_10_25.statistic}, p-value={ttest_result_10_25.pvalue}")
    print(f"{col} (u25 vs u50): Statistic={ttest_result_25_50.statistic}, p-value={ttest_result_25_50.pvalue}")
    print(f"{col} (u10 vs u50): Statistic={ttest_result_10_50.statistic}, p-value={ttest_result_10_50.pvalue}")
    print("blah " * 50)

# Perform paired t-tests
print("Paired T-Tests")
for col in columns:
    ttest_result_10_25 = ttest_rel(u10[col], u25[col])
    ttest_result_25_50 = ttest_rel(u25[col], u50[col])
    ttest_result_10_50 = ttest_rel(u10[col], u50[col])
    
    print(f"{col} (u10 vs u25): Statistic={ttest_result_10_25.statistic}, p-value={ttest_result_10_25.pvalue}")
    print(f"{col} (u25 vs u50): Statistic={ttest_result_25_50.statistic}, p-value={ttest_result_25_50.pvalue}")
    print(f"{col} (u10 vs u50): Statistic={ttest_result_10_50.statistic}, p-value={ttest_result_10_50.pvalue}")
    print("blah " * 50)
