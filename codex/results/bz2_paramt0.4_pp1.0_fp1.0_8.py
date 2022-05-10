from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(open('data/train.ft.txt.bz2', 'rb').read())

#%%
# !pip install wget
import wget
url = 'https://raw.githubusercontent.com/dmlc/web-data/master/mxnet/tinyshakespeare/input.txt'
wget.download(url, 'data/tinyshakespeare.txt')

#%%
with open('data/tinyshakespeare.txt', 'r') as f:
    raw_text = f.read()

#%%
import re
raw_text = re.sub(r'[^\x00-\x7F]+','', raw_text)

#%%
import numpy as np

#%%
chars = sorted(list(set(raw_text)))
vocab_size = len(chars)
print('total chars:', vocab_size)

#%%
char_to_idx = {ch:i for i, ch in enumerate(chars)}
idx_to_char = {i:ch for i, ch in
