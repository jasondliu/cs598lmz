from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed_data)

# +
# import zlib
# zlib.decompress(compressed_data, zlib.MAX_WBITS | 32)
# -
# import zlib
# zlib.decompress(compressed_data, zlib.MAX_WBITS | 32)

# import gzip
# gzip.decompress(compressed_data)

# # Try to simulate time
# import time
# import datetime

timestr = "2020-08-05 17:05:44"

import datetime as dt

# datetime value to string
x = dt.datetime.now()
print(x.strftime("%Y-%m-%d %H:%M:%S"))
# O/P: 2020-08-05 17:05:44

# string value to datetime
x = dt.datetime.strptime(timestr, "%Y-%m-%d %H:%M:%S")
print(x)
# O/P: 2020-08
