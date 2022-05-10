import _struct
from copy import copy
from functools import reduce
from os import _exit, getpid, remove
from os.path import exists, getmtime
from platform import system
from random import randint
from re import match
from shutil import copyfileobj
from socket import socketpair
from subprocess import Popen, PIPE
from tempfile import NamedTemporaryFile
from time import sleep

from . import _compat as five
from . import _util as util
from . import _worker as worker
from . import _version as version
from .constants import (CONN_IDLE_TIMEOUT, CONN_MAX_RETRIES, CONN_RETRY_INTERVAL,
                        CONN_TIMEOUT, CONTROL_PLANE_PORT, DATA_PLANE_PORT,
                        DIRECTION_IN, DIRECTION_OUT, FMT_ANY, FMT_BINARY, FMT_COMMAND,
                        FMT_CONTROL, FMT_ERROR, FMT_STDOUT, FMT_TEXT, FMT_VERSION,
                        PROTO_VERSION, SOCKET_TIMEOUT, STATUS
