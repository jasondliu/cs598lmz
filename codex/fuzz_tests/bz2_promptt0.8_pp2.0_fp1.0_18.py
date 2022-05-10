import bz2
# Test BZ2Decompressor to decompress the file
decompressor = bz2.BZ2Decompressor()
with open(PATH, 'rb') as input, open(PATH + ".decompressed", 'wb') as output:
    for data in iter(lambda: input.read(100 * 1024), b''):
        output.write(decompressor.decompress(data))

 
# Decompress the file without using BZ2Decompressor
with bz2.BZ2File(PATH, 'rb') as input, open(PATH + ".decompressed2", 'wb') as output:
    for data in iter(lambda: input.read(100 * 1024), b''):
        output.write(data)
print("Done")

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.options.mode.chained_assignment = None
pd.options.display.max_columns = 999

train_pkl = pd.read_pickle("./decompressed_aggregate_5ce
