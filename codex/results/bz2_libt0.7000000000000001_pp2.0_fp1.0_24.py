import bz2
bz2_file = bz2.BZ2File('/Users/wangyitong/r/xgboost/demo/data/agaricus.txt.bz2')
for line in bz2_file:
    line = line.decode("utf-8")
    print(line)

# 3.2 加载libsvm格式数据
from sklearn.datasets import load_svmlight_file
X_train, y_train = load_svmlight_file("/Users/wangyitong/r/xgboost/demo/data/agaricus.txt.train")
X_test, y_test = load_svmlight_file("/Users/wangyitong/r/xgboost/demo/data/agaricus.txt.test")

# 3.3 加载numpy sparse matrix格式数据
import numpy as np
X_train = np.random.rand(100, 5) # 训练数据是100
