from lzma import LZMADecompressor
LZMADecompressor()

"""
Baseline Python implementation
"""
import os
import pickle
import atexit
from multiprocessing import Pool, cpu_count
from datetime import datetime
from pathlib import Path

import numpy as np
