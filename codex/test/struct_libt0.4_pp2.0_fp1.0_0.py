import _struct
import _thread
import _threading_local
import _weakref
import array
import atexit
import binascii
import builtins
import cmath
import errno
import fcntl
import gc
import itertools
import math
import operator
import parser
import re
import select
import socket
import struct
import subprocess
import sys
import time
import unicodedata
import zlib

# Python 2/3 compatibility
try:
    from urllib.parse import quote_from_bytes as urlquote
    from urllib.parse import unquote_to_bytes as urlunquote
except ImportError:
    from urllib import quote as urlquote
    from urllib import unquote as urlunquote

try:
    from urllib.parse import parse_qs as _parse_qs
except ImportError:
    from cgi import parse_qs as _parse_qs

try:
    from urllib.parse import urlencode as _urlencode
except ImportError:
    from urllib import urlencode as _urlencode

