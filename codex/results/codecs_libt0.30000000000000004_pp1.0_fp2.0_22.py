import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# %%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys
import re
import time
import datetime
import warnings
import pickle
warnings.filterwarnings('ignore')

# %%

# 현재 시간 기록
now = datetime.datetime.now()
print(now)

# %%

# 현재 작업 디렉토리 확인
print(os.getcwd())

# %%

# 현재 작업 디렉토리 변경
os.chdir('C:/Users/user/Desktop/Data/Kaggle/Titanic')

# %%


