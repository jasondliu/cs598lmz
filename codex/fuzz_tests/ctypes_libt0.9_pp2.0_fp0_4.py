import ctypes
ctypes.windll.user32.SetProcessDPIAware()

import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.family'] = ['Microsoft YaHei']
plt.rcParams['font.sans-serif'] = ['SimHei']

import seaborn as sns
sns.set_style("white")

from sklearn.metrics import mean_squared_error, r2_score
def plot_regression(X, y, tmp_reg):
    plt.figure(figsize=(6,5))
    sns.regplot(X, y, line_kws={"color":"r","alpha":0.5,"lw":4})
    plt.title('Regression', fontsize=20)
    plt.xlabel(tmp_reg.x_name, fontsize=18)
    plt.ylabel(tmp_reg.y_name, fontsize=18)
    plt.tick_params(labelsize=15)  # 坐标
