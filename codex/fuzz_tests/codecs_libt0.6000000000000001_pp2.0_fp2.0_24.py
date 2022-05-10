import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

#   ---------------------------
#    IMPORT MODULES
#   ---------------------------
#   import sys
import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import math as ma
import os
import shutil as sh
import datetime as dt
import pdb

#   ---------------------------
#    FUNCTIONS
#   ---------------------------
def get_filename(file_dir, name_start, name_end):
    """
    get_filename:
    -   finds file name starting with name_start and ending with name_end in file_dir
    """
    fname = ''
    for file in os.listdir(file_dir):
        if file.startswith(name_start) and file.endswith(name_end):
            fname = file
    return fname

#   ---------------------------
#    VARIABLES
#   ------------------------
