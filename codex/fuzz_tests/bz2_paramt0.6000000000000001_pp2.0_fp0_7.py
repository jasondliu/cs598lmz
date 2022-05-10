from bz2 import BZ2Decompressor
BZ2Decompressor

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

%matplotlib inline
 
with open('amazon_reviews_us_Wireless_v1_00.tsv.bz2', 'rb') as f:
    decompressor = BZ2Decompressor()
    content = decompressor.decompress(f.read())

with open('amazon_reviews_us_Wireless_v1_00.tsv', 'wb') as f:
    f.write(content)
    
df = pd.read_csv('amazon_reviews_us_Wireless_v1_00.tsv', sep='\t', error_bad_lines=False)

df.head()

df.columns

df.shape

df.dropna(inplace=True)

df.shape

df.isnull().sum()

df['star_rating'].value_counts()

df['star_rating'] = df['star_rating'].astype('int')

df['verified
