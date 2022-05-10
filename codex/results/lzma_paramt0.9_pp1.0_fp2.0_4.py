from lzma import LZMADecompressor
LZMADecompressor().decompress(abc.encode()).decode().replace('\n','').replace('\r','')

import pandas as pd
import os
import numpy as np
from scipy.sparse import csr_matrix
import ease

# test for speed
df = pd.read_csv('F:\\cache_copy\\wx.gz', sep='\t', compression= 'gzip', chunksize= 100000, error_bad_lines=False)
for chunk in df:
    a = ease.load('F:\\cache_copy\\abc.ease')
    if int(chunk.iloc[0]['person_id']) ==67471706:
        print(chunk.iloc[0]['label'])
    if int(chunk.iloc[0]['person_id']) ==67471706 or int(chunk.iloc[1]['person_id']) ==67471706:
        print(chunk.iloc[0]['label'])
        print(chunk.iloc[1][
