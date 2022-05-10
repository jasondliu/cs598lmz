import mmap
import os
import sys
import time
import traceback

from collections import defaultdict
from ctypes import c_uint32
from datetime import datetime
from functools import partial
from glob import glob
from multiprocessing import Pool
from os.path import basename, exists, join
from subprocess import Popen, PIPE
from tempfile import NamedTemporaryFile

import numpy as np
import pandas as pd
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC

from . import __version__
from .utils import (
    get_logger,
    get_temp_file,
    get_temp_dir,
    get_temp_dir_name,
    get_temp_file_name,
    remove_temp_dir,
    remove_temp_file,
    get_files_in_dir,
    get_files_with_extension,
    get_files_with_prefix,
    get_files_with_suffix,

