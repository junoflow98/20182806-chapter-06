import numpy as np
import pandas as pd

day1_se = pd.Series(['2010-08-01','2010-08-02','2010-08-03'])
temperatures1_se = pd.Series(['28.7','25.2','22.1'])
maxwind1_se = pd.Series(['8.3','8.7','6.3'])
averagewind1_se = pd.Series(['3.4','3.8','2.9'])
df_1 = pd.DataFrame(‘일시' : day1_se, '평균기온' : temperatures1_se, '최대풍속' : maxwind1_se, '평균풍속' : averagewind1_se})
print(df_1)

day2_se = pd.Series(['2020-07-29','2020-07-30','2020-07-31'])
temperatures2_se = pd.Series(['21.6','22.9','25.7'])
maxwind2_se = pd.Series(['3.2','9.7','4.8'])
averagewind2_se = pd.Series(['1.0','2.4','2.5'])
df_2 = pd.DataFrame(‘일시' : day2_se, '평균기온' : temperatures2_se, '최대풍속' : maxwind2_se, '평균풍속' : averagewind2_se})
print(df_2)