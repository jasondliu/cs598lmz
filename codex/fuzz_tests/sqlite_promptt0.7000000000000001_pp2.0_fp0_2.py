import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/tmp/test.db").cursor().execute("CREATE TABLE test(id INTEGER PRIMARY KEY, val INTEGER);").fetchone()
import time
import subprocess
import copy
import traceback
import math
import numpy
import numpy.random
import numpy.linalg
import numpy.matlib
import scipy
import scipy.spatial
import scipy.stats
import scipy.optimize
import scipy.interpolate
import pylab
import mpmath
import random
import os
import tempfile
import re
import sys
import warnings

import dna.utils
import dna.utils.graphics
import dna.seq
import dna.io
import dna.stats

#===============================================================================
# Importing the extension module
#===============================================================================

# Load the shared library
try:
  lib = ctypes.cdll.LoadLibrary("libdnamaster.so")
except:
  lib = ctypes.cdll.LoadLibrary("../lib/libdnamaster.so")


