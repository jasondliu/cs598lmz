import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import logging
import logging.handlers
import signal
import fcntl
import re
import errno
import stat
import struct
import base64
import binascii
import tempfile
import shutil
import socket
import select
import subprocess
import hashlib
import ConfigParser
import traceback
import random

# Hack to support python 2.4
if not hasattr(__builtins__, 'any'):
    def any(iterable):
        for element in iterable:
            if element:
                return True
        return False

# Hack to support python 2.4
if not hasattr(__builtins__, 'all'):
    def all(iterable):
        for element in iterable:
            if not element:
                return False
        return True

# Hack to support python 2.4
if not hasattr(__builtins__, 'sorted'):
    def sorted(iterable):
        newlist = list(iterable)
        newlist.sort()
        return newlist

# Hack to support python
