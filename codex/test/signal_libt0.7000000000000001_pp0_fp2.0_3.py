import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Imports
import pandas as pd
import numpy as np
import math
import os
import glob
import re
import csv
import fnmatch
import operator
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.transforms as transforms
from pprint import pprint
from datetime import datetime
from collections import defaultdict, OrderedDict, namedtuple


# Define global variables
global data_dir
global out_dir
global file_type
global results
global all_files
global all_files_combined
global file_name_list
global file_count
global data_files


# Define functions
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


