import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'cp65001' else None)

# import libraries
import sys
import argparse
import re
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")

# import custom scripts
sys.path.insert(1, '../scripts')
import etl

# define parameters
data_path = '../data/raw/'
output_path = '../data/interim/'

# read data
filename = 'Other_Data.csv'
data = pd.read_csv(data_path + filename)
data.head()

# save to csv
data.to_csv(output_path + filename, index=False)
