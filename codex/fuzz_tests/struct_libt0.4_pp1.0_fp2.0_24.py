import _struct
import _sys
import _testcapi
import _thread
import _threading_local
import _time
import _warnings
import _weakref
import atexit
import errno
import faulthandler
import gc
import imp
import marshal
import math
import operator
import posix
import pwd
import pyexpat
import select
import signal
import sys
import threading
import time
import unicodedata
import zlib

# Import _thread before _threading_local to initialize the threading modules.
from _thread import *
from _threading_local import *

# This is a hack to force our _thread module to be in sys.modules so that the
# existing _thread module gets replaced with our _thread module.
sys.modules["_thread"] = sys.modules["_threading_local"]

# Import the _thread module again after the threading modules have been
# initialized.
from _thread import *

# Import _threading_local after _thread to make sure that it gets initialized
# with the same lock object as the threading modules.
from _
