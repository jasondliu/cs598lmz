import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)

# 引入所需要的库
import pymysql
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# 创建数据库连接
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/tianchi?charset=utf8mb4')

# 创建数据库连接
conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       passwd='123456',
                       db='tianchi',
                       charset='utf8mb4')

# 创建
