import mmap
import os
from pprint import pprint
import re
import subprocess
import sys
import time
from typing import Dict, List, NamedTuple, Optional, Tuple, Union

from absl import app, flags, logging
from tqdm import tqdm

from lib.data_store import DataStore
from lib.logger import Logger
from lib.utils import (
    create_dir_if_not_exists,
    create_file_if_not_exists,
    get_file_modification_timestamp,
    get_file_size,
    get_file_size_mb,
    get_file_size_pretty,
    get_file_size_pretty_mb,
    get_file_size_pretty_kb,
    get_file_size_pretty_gb,
    get_file_size_pretty_tb,
    get_files_in_dir,
    get_files_in_dir_recursively,
    get_files_in_dir_recursively_with_size,
    get_files_in_dir
