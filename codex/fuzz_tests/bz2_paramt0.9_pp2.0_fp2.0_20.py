from bz2 import BZ2Decompressor
BZ2Decompressor().decompress

import json
data = json.loads(response.decode("utf-8"))
data

import numpy as np
url = 'https://raw.githubusercontent.com/numpy/numpy/master/numpy/random/mtrand/RandomState.py'
request = urllib.request.Request(url, headers = {'User-Agent': 'Chrome/85.0.4183.121'})
response = urllib.request.urlopen(url).read()
response

import bz2
response2 = BZ2Decompressor().decompress(response)
response2

import json
data2 = json.loads(response2)
data2

num = np.arange(10000000)
print(num)

#%% sort
#%%
url = 'http://www.moneysense.gov.sg/Data/Planner/Default.aspx?DataID=CPI_MAS_MOM_CPIALLITEMS_XLS'
request = urllib.request.Request(url, headers = {'User-Agent':
