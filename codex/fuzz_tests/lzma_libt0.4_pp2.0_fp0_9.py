import lzma
lzma.LZMAFile

import os
import sys
import time
import random
import hashlib
import subprocess
import multiprocessing
import tempfile
import shutil

from collections import namedtuple

import numpy as np

from . import util
from . import archive

from .util import (
    is_string,
    is_sequence,
    is_integer,
    is_real,
    is_number,
    is_bool,
    is_iterable,
    is_callable,
    is_instance_method,
    is_instance_method_or_function,
    is_instance_method_or_function_or_callable,
    is_instance_method_or_function_or_callable_or_None,
    is_sequence_of_strings,
    is_sequence_of_integers,
    is_sequence_of_real,
    is_sequence_of_numbers,
    is_sequence_of_bools,
    is_sequence_of_iterables,
    is_sequence_of_call
