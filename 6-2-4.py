import numpy as np
import pandas as pd

day_se = pd.Series(['2013-08-08‘, '2013-08-09‘, '2013-08-10‘, '2018-07-23‘, '2018-08-04‘])
temperatures_se = pd.Series(['31.3', ‘30.6’, ‘30.6’, ‘30.5’, ‘30.3’])
maxwind_se = pd.Series(['7.8', ‘9.9’, ‘7.4’, ‘6.5’, ‘5.8’])
averagewind_se = pd.Series(['4.6', ‘6.4’, ‘3.8’, ‘1.6’, ‘3.0’])
df = pd.DataFrame(‘일시' : day_se, '평균기온' : temperatures_se, '최대풍속' : maxwind_se, '평균풍속' : averagewind_se})
print(df)