import gc, weakref
import matplotlib.cm
import warnings
from collections import namedtuple, defaultdict

import re
import os
import pkg_resources
import sys
import traceback
import linecache

def to_file(filename, text):
    with open(filename, 'wt') as f:
        f.write(text)

def to_json(filename, data):
    with open(filename, 'wt') as f:
        json.dump(data, f, indent=2)

def from_file(filename):
    with open(filename, 'rt') as f:
        return f.read()

def from_json(filename):
    with open(filename, 'rt') as f:
        return json.load(f)

def clear_thumbnail_cache(directory):
    filelist = [ f for f in os.listdir(directory) if f.startswith('thumbnail')]
    for f in filelist:
        os.remove(os.path.join(directory, f))

def itercolors(number_of_plots: int,
