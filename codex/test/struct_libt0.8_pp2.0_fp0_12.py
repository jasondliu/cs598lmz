import _struct
# import types
# import pkgutil
import sys
import inspect
import binascii
import os
import logging
from multiprocessing.pool import Pool
from multiprocessing import Value
# from ctypes import c_bool

import json
import csv
import pandas as pd
from tqdm import tqdm

# from functools import partial

from .utils import MultiProcessPool, read_object, write_object
# from .utils import count_lines_in_file
from .utils import uniq_list, is_hex_str, is_hex_str_or_empty, create_file_path
from .models import McfCommand
from .utils import ConfigFile
from . import _constants
# from typing import Union


INPUT_DIR = _constants.INPUT_DIR
OUTPUT_DIR = _constants.OUTPUT_DIR


# def create_file_path(file_name: str, suffix: str='.csv') -> str:
#     """
#     Create file with path and suffix.
#     :param file_
