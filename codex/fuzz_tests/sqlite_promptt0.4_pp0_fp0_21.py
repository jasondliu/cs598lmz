import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('file::memory:?cache=shared')
import os
import time
import sys
import platform
import multiprocessing
import multiprocessing.sharedctypes
import traceback

import numpy as np

import logging
logger = logging.getLogger(__name__)

# TODO:
# - fix: if the process is killed, the shared memory is not freed
# - test: if the process is killed, the shared memory is not freed
# - test: if the process is killed, the shared memory is not freed
# - test: if the process is killed, the shared memory is not freed
# - test: if the process is killed, the shared memory is not freed
# - test: if the process is killed, the shared memory is not freed
# - test: if the process is killed, the shared memory is not freed
# - test: if the process is killed, the shared memory is not freed
# - test: if the process is killed, the shared memory is not freed
# - test: if the process is killed, the shared memory is not freed
# - test: if the process is killed, the
