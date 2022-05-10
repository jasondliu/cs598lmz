import mmap
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import traceback
from collections import namedtuple
from contextlib import contextmanager
from datetime import datetime
from functools import wraps
from itertools import islice
from multiprocessing import Process, Queue, cpu_count
from pathlib import Path
from typing import Callable, Dict, Iterator, List, Optional, Tuple, Union, cast

import click
import yaml
from yaml.error import YAMLError

from . import __version__
from .cwl import CWL_VERSION
from .utils import (
    CWL_TOOL_PATH,
    CWL_TOOL_PATH_DEFAULT,
    CWL_TOOL_PATH_ENV,
    CWL_TOOL_PATH_HELP,
    CWL_TOOL_PATH_VAR,
    CWL_WORKFLOW_PATH,
    CWL_WORKFLOW_PATH_DEFAULT,
    CWL_WORKFLOW_PATH_ENV,
