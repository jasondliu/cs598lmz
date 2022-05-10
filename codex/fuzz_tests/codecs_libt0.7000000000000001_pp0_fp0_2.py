import codecs
codecs.setDefaultEncoding("utf-8")

# 屏蔽警告
import warnings
warnings.filterwarnings("ignore")

# 导入数据分析常用库
import numpy as np
import pandas as pd

# 导入可视化库
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use("ggplot")
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 导入数据预处理库
from sklearn.preprocessing import LabelEncoder

# 导入sklearn中的建模和评
