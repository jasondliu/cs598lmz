import socket
import sys
import time

from . import constants
from . import exceptions
from . import utils
from . import version

try:
    import ssl
except ImportError:
    ssl = None

try:
    import resource
except ImportError:
    resource = None

try:
    import fcntl
except ImportError:
    fcntl = None

try:
    import select
except ImportError:
    select = None

try:
    import queue
except ImportError:
    import Queue as queue

try:
    import threading
except ImportError:
    threading = None

try:
    import multiprocessing
except ImportError:
    multiprocessing = None

try:
    import multiprocessing.connection
except ImportError:
    multiprocessing = None

try:
    import multiprocessing.reduction
except ImportError:
    multiprocessing = None

try:
    import multiprocessing.managers
except ImportError:
    multiprocessing = None

