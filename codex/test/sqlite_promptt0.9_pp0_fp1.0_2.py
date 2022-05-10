import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
# conn = sqlite3.connect("/Users/songhailun/Desktop/Algo_TimeBar.db3", timeout=10)
# c = conn.cursor()
# c.execute("SELECT * FROM `TimeBar`")
# for row in c:
#     print("id:%s"%(row[0]))
# conn.close()

# Test pyalgotrade
from pyalgotrade.recommend import Recommender
import copy
import pymysql
import os
import logging
from pyalgotrade.talibext import indicator
import pandas as pd
# from sklearn.externals import joblib
# from sklearn.linear_model import LogisticRegressionCV
# from sklearn.linear_model.logistic import LogisticRegression
import demjson
# from pyalgotrade.recommend import *
import pyalgotrade.myUtil
import pyalgotrade.myCom
import pyalgotrade.myMath

#
# 股票日线回测交易模
