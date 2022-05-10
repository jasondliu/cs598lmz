import ctypes
ctypes.cast(0, ctypes.py_object)

# SOURCE LINE 2

import sys
import os
import re
import time
import logging
import threading
import traceback
import signal
import subprocess
import multiprocessing

from multiprocessing import Process, Queue, Pipe
from Queue import Empty

import pkg_resources

from IPython.utils.traitlets import (
    Instance, Dict, List, Unicode, Int, Bool, Any, Type,
    CaselessStrEnum,
)
from IPython.utils.importstring import import_item
from IPython.utils.py3compat import string_types
from IPython.utils.text import indent, wrap_paragraphs
from IPython.utils.warn import warn, error
from IPython.utils.process import arg_split
from IPython.utils.path import filefind, get_ipython_dir
from IPython.utils.localinterfaces import LOCALHOST
from IPython.utils.jsonutil import json_clean
from IPython.utils.frame import extract_module_locals
from IP
