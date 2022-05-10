import weakref

from . import _core
from . import _util
from . import _errors
from . import _types
from . import _constants
from . import _compat
from . import _lib
from . import _ffi
from . import _cdata
from . import _rawffi
from . import _callbacks
from . import _buffer
from . import _thread
from . import _version

from . import _lazyimport

_lazyimport.lazyimport(globals(), """
import sys
import os
import warnings
import threading
import traceback
import collections
import contextlib
import functools
import operator
import struct
import itertools
import weakref
import io
import gc
import types
import numbers
import abc
import collections.abc
import datetime
import time
import re
import array
import binascii
import base64
import zlib
import hashlib
import hmac
import random
import socket
import select
import errno
import fcntl
import platform
import locale
import ctypes
import ctypes.util
import
