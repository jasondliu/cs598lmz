import lzma
lzma.decompress()
"""

import os
import sys
import multiprocessing
import subprocess
import csv
import gzip
import re
import argparse
import glob
import textwrap
import shutil
import copy
import logging
import pickle
import pysam
import pandas as pd
import numpy as np
import h5py


# import custom modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import python_tools
from python_tools import start_logger
from python_tools import Mapper_Record


def is_gzipped(filename):
    """
    Returns True if the file is gzipped.
    """
    with open(filename, 'rb') as test_f:
        return bin(test_f.read(2)[0])[2:].zfill(8)[0] == '1'


def get_read_ids(read_ids_file):
    """
    Gets list of read IDs from file.
    """
    read
