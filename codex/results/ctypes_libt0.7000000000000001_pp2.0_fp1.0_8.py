import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)

import matplotlib as mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 定义显示中文
myfont = FontProperties(fname=r'C:\Windows\Fonts\simfang.ttf')

# 显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
# 用来正常显示负号
plt.rcParams['axes.
