import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[1;32m')).start()

try:
    import readline
except ImportError:
    print "Module readline not available."
else:
    import rlcompleter
    readline.parse_and_bind("tab: complete")

import os

pwd = os.getcwd()

print 'Welcome to the Jupyter Notebook.'
print 'The current working directory is:'
print pwd

def relpath(folder):
    return os.path.join(pwd, folder)

import numpy as np
import pandas as pd

def file_len(filename):
    with open(filename) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def csv_len(filename):
    return sum(1 for line in open(filename)) - 1

def list_to_string(mylist):
    '''
    Convert a list to a string, removing commas and brackets.

    Parameters
    ----------
    mylist
