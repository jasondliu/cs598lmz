import ctypes
ctypes.cast(0, ctypes.py_object)

#import os
#os.environ["PYTHONSTARTUP"] = "~/.pythonrc"

import sys
sys.ps1 = '\033[1;32m>>> \033[0m'
sys.ps2 = '\033[1;32m... \033[0m'

import numpy as np
import pandas as pd
