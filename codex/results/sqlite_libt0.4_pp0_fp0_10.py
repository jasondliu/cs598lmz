import ctypes
import ctypes.util
import threading
import sqlite3
import os
import sys
import time
import fcntl
from datetime import datetime
import json
import socket
from collections import OrderedDict
from functools import wraps
from subprocess import Popen, PIPE
from threading import Thread
from Queue import Queue, Empty

from lib.common.abstracts import Package
from lib.api.process import Process
from lib.common.results import NetlogFile
from lib.common.exceptions import CuckooPackageError
from lib.common.defines import KERNEL32, PIPE_ACCESS_DUPLEX, PIPE_TYPE_MESSAGE, PIPE_READMODE_MESSAGE, PIPE_WAIT, PIPE_REJECT_REMOTE_CLIENTS, PIPE_UNLIMITED_INSTANCES, ERROR_PIPE_CONNECTED, ERROR_PIPE_BUSY, ERROR_SEM_TIMEOUT, ERROR_PIPE_LISTENING, ERROR_PIPE_NOT_CONNECTED, INVALID_HANDLE_
