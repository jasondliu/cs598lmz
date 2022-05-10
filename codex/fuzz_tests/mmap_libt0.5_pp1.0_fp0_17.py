import mmap
import os
import re
import sys
import time
import traceback
import warnings
from collections import OrderedDict
from datetime import datetime
from functools import partial
from io import BytesIO
from multiprocessing import cpu_count
from threading import Thread
from typing import Any, Callable, Dict, List, Optional, Tuple, Union

from tqdm.auto import tqdm
from tqdm.contrib.concurrent import process_map

from ..utils import (
    _decode_unicode,
    _encode_unicode,
    _get_file_size,
    _get_files_from_path,
    _get_files_from_path_generator,
    _get_files_from_path_generator_with_progressbar,
    _get_files_from_path_with_progressbar,
    _get_files_from_paths,
    _get_files_from_paths_generator,
    _get_files_from_paths_generator_with_progressbar,
    _
