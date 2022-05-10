import bz2
bz2.decompress(bz2_data)

# 使用zlib压缩数据
import zlib
s = b'witch which has which witches wrist watch'
len(s)
t = zlib.compress(s)
len(t)
zlib.decompress(t)
zlib.crc32(s)

# 利用pandas处理时间序列
from datetime import datetime
from pandas import Series, DataFrame
import pandas as pd; import numpy as np
now = datetime.now()
now
now.year, now.month, now.day
delta = datetime(2011, 1, 7) - datetime(2008, 6, 24, 8, 15)
delta
delta.days
delta.seconds
from datetime import timedelta
start = datetime(2011, 1, 7)
start + timedelta(12)
start - 2 * timedelta(12)
stamp = datetime(2011, 1, 3)
str(
