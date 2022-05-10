import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

# import modules
# import openpyxl
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import glob, os

# load data
os.chdir("D:/Dropbox/Github/data/sample_data/excel")
df = pd.read_excel("sample3.xlsx", sheet_name="sample1") # load 1 sheet
df2 = pd.read_excel("sample3.xlsx", sheet_name=0) # load 1 sheet
df3 = pd.read_excel("sample3.xlsx", usecols="A,B") # load A and B column
# print(df3)

df4 = pd.read_excel("sample3.xlsx", sheet_name="sample1", index_col=0) # load 1 sheet and set 1st column as index
#
