import _struct
import _thread
import _threading
import _tracemalloc
import _turbo
import _weakref
import _weakrefset
import _winapi

import array
import audioop
import binascii
import builtins
import cmath
import errno
import faulthandler
import fcntl
import fractions
import grp
import itertools
import operator
import os
import parser
import resource
import select
import signal
import socket
import stat
import stringprep
import struct
import subprocess
import sys
import sysconfig
import termios
import time
import unicodedata
import xxsubtype
import zipimport

# _testcapi is not built by default, import it only if it is present
if hasattr(sys.modules[__name__], "_testcapi"):
    import _testcapi

# _testbuffer is not built by default, import it only if it is present
if hasattr(sys.modules[__name__], "_testbuffer"):
    import _testbuffer

# _testimportmultiple is not built by default, import it
