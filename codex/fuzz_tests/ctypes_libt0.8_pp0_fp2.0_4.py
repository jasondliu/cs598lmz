import ctypes
ctypes.cdll.LoadLibrary('../datascience/datascience/src/libgsl.so')
ctypes.cdll.LoadLibrary('../datascience/datascience/src/libgslcblas.so')
import sys
sys.path.append('../datascience')
from datascience import *

%matplotlib inline
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')
import numpy as np
 
from client.api.notebook import Notebook
ok = Notebook('hw05.ok')
 
_ = ok.auth(inline=True, force=True)
 
from client.api.notebook import Notebook
ok = Notebook('hw05.ok')
_ = ok.auth(inline=True)
 
 
 
 
 
 

# ## 1. Catching Cheaters
red_toenail_polish = 1/200000
red_toenail_polish_and_caught_cheating = 1/10000000

posterior = red_toenail_
