import mmap
import os
import sys
import threading
import time

from ctypes import *

try:
    from cStringIO import StringIO
except ImportError:
    from io import StringIO

try:
    import resource
except ImportError:
    resource = None

