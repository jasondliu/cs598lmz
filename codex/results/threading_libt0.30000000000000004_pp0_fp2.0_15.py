import threading
threading.stack_size(1024*1024*1024)

# import dependencies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time
import csv
import os
import sys
import datetime
import re
import pickle
import warnings
warnings.filterwarnings('ignore')

# import custom modules
sys.path.append('../')
import modules.data_import as data_import
import modules.data_cleaning as data_cleaning
import modules.data_analysis as data_analysis
import modules.data_visualization as data_visualization
import modules.data_export as data_export

# import data
data_path = '../data/'
data_file = 'data_cleaned.csv'
df = data_import.import_data(data_path, data_file)

# create dataframe with only relevant columns
df = df[['id', 'title', 'description', 'price', 'location', 'category', 'subcategory', 'brand', 'condition', 'delivery', 'created
