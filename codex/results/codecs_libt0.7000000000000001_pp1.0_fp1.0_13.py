import codecs
codecs.register(lambda name: name == 'cp65001' and codecs.lookup('utf-8') or None)

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from sklearn import svm

# 导入数据
path = '9.Receiver Operating Characteristic (ROC)\\'
data = pd.read_csv(path + 'data.csv', encoding='utf-8')
train_x = data[['年龄', '有工作', '有自己的房子', '信贷情况']]
train_y = data['有房贷']

# 创建svm分类器
model = svm.SVC(kernel='linear')
model.fit(train_x, train_y)

# 获取svm函数中的w
w = model.coef_[0]
a = -
