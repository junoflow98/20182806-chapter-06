import numpy as np
import pandas as pd

day_se = pd.Series(['2013-08-08‘])
temperatures_se = pd.Series(['31.3'])
maxwind_se = pd.Series(['7.8'])
averagewind_se = pd.Series(['4.6'])
df = pd.DataFrame(‘일시' : day_se, '평균기온' : temperatures_se, '최대풍속' : maxwind_se, '평균풍속' : averagewind_se})
print(df)