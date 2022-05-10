import mmap
import numpy as np
import pandas as pd
import sys

### SETTINGS ###

# Number of bytes in single filter element
bytes_filter = 8

# Frequency of information about the progress
info_freq = 10000

# Indexes of needed columns of the data
cols = [0, 1, 3]

### END OF SETTINGS ###

### FUNCTIONS ###

# Calculates EPS for a single filter
def calc_eps(mmap_fil, index_fil_1, index_fil_2, el_fil_1, el_fil_2):
    if el_fil_2 != el_fil_1:
        return 0
    else:
        if index_fil_1<index_fil_2:
            mmap_fil.seek(2 * bytes_filter * index_fil_1)
            filter_1 = mmap_fil.read(2 * bytes_filter)
            mmap_fil.seek(2 * bytes_filter * index_fil_2)
