import _struct
import _symtable
import array
import binascii
import fcntl
import inspect
import linecache
import posix
import re
import select
import subprocess
import sys
import token
import tokenize
import trace
import traceback
import types
import warnings
import _weakref

# we're not going to support the imp module at all, as it's likely to
# not even be executable by third party modules.

# Only modules that have to be imported before builtin one should go here.
# More of them will be moved later, but for example signal is the core
# system module, so it should stay here for a while.
import signal

# CPython module state
_ignore_missing_imports = True

##from _types import ModuleType

def _fix_co_filename(value, oldfilename):
    """Maps the new filename to oldfilename."""
    try:
        return value._fix_co_filename(oldfilename) # string
    except AttributeError:
        value = value.rpartition('.') # tuple
        map = _co_filename_
