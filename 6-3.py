import numpy as np
import pandas as pd

a1_se = pd.Series(['A0','A1','A2'])
b1_se = pd.Series(['B0','B1','B2'])
c1_se = pd.Series(['C0','C1','C2'])
d1_se = pd.Series(['D0','D1','D2'])
df_1 = pd.DataFrame({'A' : a1_se, 'B' : b1_se, 'C' : c1_se, 'D' : d1_se})
print(df_1)

b1_se = pd.Series(['B0','B1','B2'])
c1_se = pd.Series(['C0','C1','C2'])
d1_se = pd.Series(['D0','D1','D2'])
e1_se = pd.Series(['E0','E1','E2'])
df_2 = pd.DataFrame({'B' : b1_se, 'C' : c1_se, 'D' : d1_se, 'E' : e1_se})
print(df_2)