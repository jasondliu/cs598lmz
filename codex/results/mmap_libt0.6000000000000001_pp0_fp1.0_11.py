import mmap
import struct
import array
import sys
import os
import os.path
import glob
import time
import random
import re
import math
import shutil
import datetime

# from scipy import *
# from scipy import linalg
import numpy as np
# from numpy import *
# from numpy.linalg import *

from scipy.sparse import *
from scipy.sparse.linalg import *

from mpi4py import MPI
from mpi4py.MPI import ANY_SOURCE

from subprocess import *

comm = MPI.COMM_WORLD

my_id = comm.Get_rank()
num_procs = comm.Get_size()

# print my_id, num_procs

# sys.path.append('/home/jkent/src/python/numpy') 
# import numpy as np

# sys.path.append('/home/jkent/src/python/scipy') 
# from scipy import *
# from scip
