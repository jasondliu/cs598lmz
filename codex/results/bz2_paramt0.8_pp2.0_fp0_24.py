from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed)

# source: https://www.reddit.com/r/python/comments/1nhf1n/decompressing_bz2_files/
# import gzip
# import shutil
# with gzip.open('yourfile.gz', 'rb') as f_in:
#     with open('yourfile.csv', 'wb') as f_out:
#         shutil.copyfileobj(f_in, f_out)

# import bz2
# import shutil
# with bz2.open("yourfile.txt.bz2", 'r') as f_in:
#     with open("yourfile.txt", 'wb') as f_out:
#         shutil.copyfileobj(f_in, f_out)

# source: https://stackoverflow.com/questions/45459007/add-column-to-pandas-dataframe-with-series-of-list
# import pandas as pd
# lst = ['b', 'c']
# df = pd.DataFrame
