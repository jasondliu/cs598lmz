import select
import signal
import socket
import sys
import threading
import time
import urllib


try:
    import ssl
except ImportError:
    ssl = None

try:
    import OpenSSL
except ImportError:
    OpenSSL = None

try:
    import pwd
except ImportError:
    pwd = None

try:
    import grp
except ImportError:
    grp = None

try:
    import resource
except ImportError:
    resource = None

try:
    import fcntl
except ImportError:
    fcntl = None

try:
    import termios
except ImportError:
    termios = None

try:
    from io import BytesIO as IO
except ImportError:
    from cStringIO import StringIO as IO

try:
    xrange
except NameError:
    xrange = range

try:
    import __builtin__
except ImportError:
    import builtins as __builtin__

try:
    callable = __builtin__.callable

