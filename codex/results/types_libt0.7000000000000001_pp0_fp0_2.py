import types
types.ModuleType('matplotlib')

import matplotlib.pyplot as plt
import numpy as np

# 配置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 显示图例
plt.rcParams['legend.fancybox'] = True

# 支持中文
plt.rcParams['font.family'] = 'sans-serif'

# 设置字体大小
plt.rcParams['font.size'] = 15

# 支持中文
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

# 支持负号
plt.rcParams['axes.unicode_minus'] = False

# 这个是坐标
