import bz2
bz2_file = bz2.fncompress(word_data)
print(len(bz2_file))

# 51,658 vs the original file at 100,660 bytes.

import numpy as np

np.mean(word_data)

np.var(word_data)

np.std(word_data)

# Standard deviation is 6.6

import pandas as pd

pd.DataFrame(word_data)

# 3 most common words:
# the, and you

# Least common word:
# 'unconversational'

# That sounds about right

import re

for word in range(len(word_data)):
    if re.match("[A-Za-z]+",word_data[word]) != None:
        print(word_data[word])

# There are 158,218 words in this file.

# Write a function called `calc_running_median` that takes a list as input and returns a list of medians. Your function should use the `running_median` function that you defined
