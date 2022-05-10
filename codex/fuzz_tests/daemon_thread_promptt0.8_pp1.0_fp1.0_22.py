import threading
# Test threading daemon
import datetime
# For storing data
import sqlite3
# For plotting
import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
# For plotting colors
import colorsys
# For computing random colors
import random
import itertools
# For timestamping the beginning of each movie
import time
# For making a symbolic link
import os
# For plotting on the same axis
#import pandas as pd
# For reshaping
import numpy as np

# To measure execution time
import time

# IMPORTANT!
# We need to do this because of a bug in the threading module
# See http://bugs.python.org/issue8844
import threading
threading._DummyThread._Thread__stop = lambda x: 42

# To read the parameters from the command line
# See http://docs.python.org/2/library/argparse.html
import argparse

# To measure the execution time
import time

# To
