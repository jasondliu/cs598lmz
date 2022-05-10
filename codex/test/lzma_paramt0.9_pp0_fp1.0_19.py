from lzma import LZMADecompressor
LZMADecompressor()

import time
start = time.time()
# Create a JSON file, in which the output will be stored.
fp = open('hong_kong_sar_china.json', 'w')

# Type of the file, which we are going to read.
filename = 'hong_kong_sar_china.csv'

# We need this in order to be able to identify the type of each cell.
