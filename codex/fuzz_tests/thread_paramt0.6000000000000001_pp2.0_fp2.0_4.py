import sys, threading
threading.Thread(target=lambda: sys.stdout.write('\x1b[1;32m' + '\n'.join(filter(lambda s: s.startswith('[DEBUG]'), sys.stdin.read().splitlines(True))) + '\x1b[0m')).start()

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
import matplotlib.colors as colors
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
from matplotlib.collections import PatchCollection
from matplotlib import cm
import matplotlib.image as mpimg
from matplotlib.colors import LogNorm

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB
