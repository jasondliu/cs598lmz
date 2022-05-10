import codecs
codecs.open('../../data/train_set.csv', 'r', 'utf-8')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

train_data = pd.read_csv('../../data/train_set.csv')
test_data = pd.read_csv('../../data/test_set.csv')

train_data.head()

# 查看数据类型
train_data.dtypes

# 查看数据信息
train_data.info()

# 查看缺失值
train_data.isnull().sum()

# 查看数据统计信息
train_data.describe()

# 查看article和class的具体信息
train_data['article'][0]
train_data['class
