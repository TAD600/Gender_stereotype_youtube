def main():
    pass


import pandas as pd
from scipy.stats import mannwhitneyu
from scipy.stats import kruskal


test = pd.read_csv('FINAL.csv')

m = test[test['gender'] == 0]
f = test[test['gender'] == 1] 
m_compound = m['compound']
f_compound = f['compound']

# Mann-Whitney U Test 
# Gender
result = mannwhitneyu(f_compound, m_compound, alternative='two-sided')
U_statistic = result.statistic
n1 = len(f_compound)
n2 = len(m_compound)
U_expected = n1 * n2 / 2
U_alternate = n1*n2 - U_statistic
sigma_U = (n1 * n2 * (n1 + n2 + 1) / 12) ** 0.5
z_statistic = (U_statistic - U_expected) / sigma_U
r = U_statistic / (n1 * n2)
print(f"U Statistic: {U_statistic}")
print(f"U Alternate: {U_alternate}")
print(f"Z Statistic: {z_statistic}")
print(f"P-Value: {result.pvalue}")
print(f"Effect size: {r}")

# Language
b = test[test['language'] == 1]
e = test[test['language'] == 0] 
b_compound = b['compound']
e_compound = e['compound']

result1 = mannwhitneyu(b_compound, e_compound, alternative='two-sided')
U_statistic1 = result1.statistic
n3 = len(b_compound)
n4 = len(e_compound)
U_expected1 = n3 * n4 / 2
U_alternate1 = n3*n4 - U_statistic1
sigma_U1 = (n3 * n4 * (n3 + n4 + 1) / 12) ** 0.5
z_statistic1 = (U_statistic1 - U_expected1) / sigma_U1
r1 = U_statistic1 / (n3 * n4)
print(f"U Statistic: {U_statistic1}")
print(f"U Alternate: {U_alternate1}")
print(f"Z Statistic: {z_statistic1}")
print(f"P-Value: {result1.pvalue}")
print(f"Effect size: {r1}")

# Kruskal-Wallis H Test 
# Gender
h_statistic3, p_value = kruskal(f_compound, m_compound)
k = 2
n = len(test)
e = h_statistic3-k+1
l = n - k
effect= e/l
print(f"chi square: {h_statistic3}")
print(f"P-Value: {p_value}")
print(f"Effect size: {effect}")

# Language
h_statistic4, p_value1 = kruskal(b_compound, e_compound)
k = 2
n = len(test)
e1 = h_statistic4-k+1
l = n - k
effect1= e1/l
print(f"chi square: {h_statistic4}")
print(f"P-Value: {p_value1}")
print(f"Effect size: {effect1}")