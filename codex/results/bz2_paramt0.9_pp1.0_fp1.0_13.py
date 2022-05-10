from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'\x42\x5a\x68')

from itertools import *
print(_)

from hashlib import md5
for line in open('../script_data/somefile.txt'):
    line = line.rstrip()
    if line.startswith('#'):
        continue
    h = md5.copy()
    h.update(line)
    print(h.hexdigest())

import pandas as pd
df = pd.read_csv("../script_data/https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv")
df

from collections import deque
dq = deque('You shall not pass')
print(dq)

'''
