import codecs
codecs.register_error('replace2', lambda e:'输入了含有不能解码的字符')
import os
import pandas as pd
import pickle
import random
import re
import string
import time
import zipfile
from opencc import OpenCC
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
import csv
import argparse
import jieba


my_seed = 2019
random.seed(my_seed)
np.random.seed(my_seed)

stopwords = open('stopwords.txt', encoding='utf-8').readlines()
# 读入xlsx打开但是无法正常处理
# xl = pd.ExcelFile('gldjc_cwsfz_v2_20w.xlsx')
# df = xl.parse('Sheet1')
with open('gldjc_cwsfz_v2_20w.csv', 'r') as f:
   
