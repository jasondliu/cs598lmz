import ctypes
import ctypes.util
import threading
import sqlite3
import json
import re
import os, sys
import tempfile
import socket
import struct
import sqlalchemy
import pickle
import shutil
import traceback
import contextlib

from base64 import b64encode, b64decode

from . import slog
import ffn

# type definitions

COID_T = ctypes.c_char_p
CO_LONG_LONG_T = ctypes.c_longlong
CO_BOOL_T = ctypes.c_int
CO_RC_T = ctypes.c_ubyte
CO_ANODE_HDL_T = ctypes.c_void_p
CO_INODE_NUM_T = ctypes.c_ushort
CO_DATABRICK_NUM_T = ctypes.c_ushort
CO_INDEX_T = ctypes.c_ushort
CO_RECORD_NUM_T = ctypes.c_ushort
CO_RECORD_STR_T = ctypes.c_char_p
CO_COMM_HDL_T = ctypes.c
