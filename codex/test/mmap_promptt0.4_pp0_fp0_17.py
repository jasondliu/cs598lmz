import mmap
# Test mmap.mmap.readline()
import os
import re
import shutil
import signal
import socket
import stat
import string
import struct
import subprocess
import sys
import tempfile
import threading
import time
import traceback

# In some cases (e.g. Solaris) the system's fcntl module is
# broken.  In those cases we can use the fcntl module from
# Python's standard library.
try:
    import fcntl
except ImportError:
    import FCNTL as fcntl

# In some cases (e.g. Solaris) the system's termios module is
# broken.  In those cases we can use the termios module from
# Python's standard library.
try:
    import termios
except ImportError:
    import TERMIOS as termios

# In some cases (e.g. Solaris) the system's resource module is
# broken.  In those cases we can use the resource module from
# Python's standard library.
try:
    import resource
except ImportError:
    import RESOURCE as resource

#
