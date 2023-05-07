import numpy as np
import pandas as pd

income={'a' : 32, 'b' : 13, 'c' : 68, 'd' : 51, 'e' : 13}
income_se = pd.Series(income)
print(income_se)

m_idx = np.argmax(income_se)
print('num_series의 최대값:', month_se[m_idx])