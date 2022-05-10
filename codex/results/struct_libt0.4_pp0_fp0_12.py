import _struct
import _thread
import _threading
import _time
import _warnings
import _weakref
import array
import atexit
import builtins
import errno
import fcntl
import gc
import grp
import itertools
import marshal
import math
import operator
import os
import pwd
import re
import select
import signal
import sys
import time
import traceback
import types
import unicodedata
import zipimport
import zlib

# this is a list of modules which are known to be non-reentrant
# and thus cannot be used from signal handlers
non_reentrant_modules = [
    _thread, _threading, _queue, _socket, _ssl, _signal,
    _contextvars, _multiprocessing, _multiprocessing.connection,
    _multiprocessing.heap, _multiprocessing.managers,
    _multiprocessing.process, _multiprocessing.reduction,
    _multiprocessing.semaphore_tracker, _multip
