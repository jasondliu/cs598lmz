import ctypes
import ctypes.util
import threading
import sqlite3
import time
import datetime
import sys, getopt
import statistics
import numpy as np
from numpy import genfromtxt
import time
from scipy.stats import norm
import scipy.stats as stats

###############################################################################################
#   Copyright (c) 2017-2019, The University of Texas at Austin & University of California, Merced.
#
#   This file is part of the libcem library.
#
#   libcem is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   libcem is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
