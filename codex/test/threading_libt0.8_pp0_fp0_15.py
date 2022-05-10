import threading
threading.stack_size(2**27)
import sys
import graph_tool.all as gt
import time
import os
import math
from functools import partial
import argparse
from multiprocessing import Pool
from multiprocessing import cpu_count

class c:
  PURPLE = '\033[95m'
  CYAN = '\033[96m'
  DARKCYAN = '\033[36m'
  BLUE = '\033[94m'
  GREEN = '\033[92m'
  YELLOW = '\033[93m'
  RED = '\033[91m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  END = '\033[0m'

def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1")

def update_progress(progress):
    barLength = 25 # Modify this to change the length of the progress bar
