import mmap
import os
import socket
import struct
import subprocess
import sys

# Try to import the Python 2 modules and fallback to Python 3 if necessary.
try:
    from ConfigParser import ConfigParser
    from Queue import Queue
except ImportError:
    from configparser import ConfigParser
    from queue import Queue

# Import our own modules.
