import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# import csv
# csv.field_size_limit(sys.maxsize)

# import os
# os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

# import pandas as pd
# pd.set_option('display.max_columns', None)

# import numpy as np
# np.set_printoptions(threshold=np.inf)

# import matplotlib.pyplot as plt
# %matplotlib inline
# plt.rcParams['figure.figsize'] = (15, 6)
# plt.rcParams['font.sans-serif']=['SimHei']
# plt.rcParams['axes.unicode_minus']=False

# import seaborn as sns
# sns.set(font='SimHei')

# import warnings
# warnings.filterwarnings('ignore')


