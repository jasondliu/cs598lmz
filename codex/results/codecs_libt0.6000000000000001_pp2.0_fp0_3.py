import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

#%%
import os
import sys
import glob
import re
import pandas as pd
import numpy as np
from datetime import datetime
from xlsxwriter.workbook import Workbook
import time
import csv
from datetime import timedelta
import xlrd

#%%
def convert_date(date):
    """
    This function converts date to a format that is readable by excel.
    """
    date = date[:6]
    date = date[:4] + '/' + date[4:6] + '/' + date[-2:]
    return date

#%%
def get_data_from_excel(path):
    """
    Reads data from excel file.
    """
    DATAFILE = path
    data = pd.read_excel(DATAFILE)
    return data

#%%
def get_data_from_csv(path):
    """
    Reads data from c
