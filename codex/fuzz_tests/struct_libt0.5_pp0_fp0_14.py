import _struct
import _thread
import _threading_local
import _time
import _warnings
import _weakref
import errno
import imp
import itertools
import marshal
import math
import operator
import os
import posix
import pwd
import py_compile
import random
import re
import select
import signal
import socket
import stat
import string
import sys
import sysconfig
import tempfile
import termios
import time
import unicodedata
import unittest
import zipimport

# This is a list of builtin modules that should not be replaced by user code
# when using "from __future__ import absolute_import".
_allowed_modules = frozenset([
    '__builtin__', '__main__', '_ast', '_bisect', '_codecs', '_codecs_cn',
    '_codecs_hk', '_codecs_iso2022', '_codecs_jp', '_codecs_kr',
    '_codecs_tw', '_collections', '_csv', '_fun
