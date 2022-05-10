import mmap
import numpy as np
import os
import sys
import time

from multiprocessing import Process, Queue

from . import constants
from . import util
from . import util_cpp
from . import util_cython
from . import util_python

from .util import (
    get_file_size,
    get_num_lines,
    get_num_lines_mmap,
    get_num_lines_python,
    get_num_lines_python_mmap,
    get_num_lines_python_mmap_chunk,
    get_num_lines_python_mmap_chunk_numpy,
    get_num_lines_python_mmap_numpy,
    get_num_lines_python_mmap_numpy_chunk,
    get_num_lines_python_mmap_numpy_chunk_numpy,
    get_num_lines_python_mmap_numpy_numpy,
    get_num_lines_python_mmap_numpy_numpy_chunk,
    get_
