import mmap
from zipfile import ZipFile
import xlrd
import pandas
import functools
from functools import reduce
import pymysql
from datedelta import datedelta
import datetime as dt
import os
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
import seaborn as sns
import matplotlib.pyplot as plt
from unicodedata import numeric
import operator


path = 'C:\\'

# Files
models_file = ('C:\\fwd_models.csv')
zip_file = ('C:\\WINALS-MV-INPUT.zip')
