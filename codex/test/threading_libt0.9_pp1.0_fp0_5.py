import threading
threading.stack_size(2**27)
import sys

# 2. Import libraries and modules
import numpy as np
import pandas as pd

# 3. Load the dataset
dataset = pd.read_csv('./gamesales.csv')

# 4. Preprocess input data

# 4.1 Represent Sales as a categorical variable
rankings = []

for line in dataset:
    if line['Global_Sales'] > 19.5:
        rankings.append('5')
    elif line['Global_Sales'] > 9.5:
        rankings.append('4')
    elif line['Global_Sales'] > 4.5:
        rankings.append('3')
    elif line['Global_Sales'] > 2.35:
        rankings.append('2')
    elif line['Global_Sales'] > 0.8:
        rankings.append('1')
    elif line['Global_Sales'] < 0.8:
        rankings.append('0')

dataset['Sales_Rank'] = rankings

# 4.2 Delete Sales
del dataset
