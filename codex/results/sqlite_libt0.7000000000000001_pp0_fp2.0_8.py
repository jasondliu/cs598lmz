import ctypes
import ctypes.util
import threading
import sqlite3
import time

from sqlite3 import OperationalError

import os
import sys

import requests

import pyinotify

from database import *
from mail import *

FILE_CREATED = pyinotify.EventsCodes.IN_CLOSE_WRITE
FILE_DELETED = pyinotify.EventsCodes.IN_DELETE

#
# Данные по ядру и библиотеке
#

class LSP_REVISION (Structure):
    _fields_ = [
        ('major', c_uint),
        ('minor', c_uint)
    ]

class LSP_PARAM (Structure):
    _fields_ = [
        ('size', c_size_t),
        ('revision', LSP_REVISION)
    ]

class LSP_HANDLE (Structure):
    _fields_ = [
        ('context', c_void_p)
    ]

class LSP_FILE_ID (Structure
