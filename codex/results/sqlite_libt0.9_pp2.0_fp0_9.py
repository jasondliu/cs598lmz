import ctypes
import ctypes.util
import threading
import sqlite3
import os

from .utils import (monkeypatch,
                    find_function_ondisk,
                    existing_dev_point,
                    get_first_line,
                    generate_label)
from . import (db,
               device_data,
               vendor_data,
               model_data)

#
# Some global declarations
#
libblkid_path = ctypes.util.find_library("blkid")

libblkid = ctypes.CDLL(libblkid_path)

lock = threading.RLock()

#
# Internal constants
#
BLKID_VERSION_MAJOR  = 1
BLKID_VERSION_MINOR  = 1
BLKID_VERSION_PATCH  = 0

BLKID_PROBTYPE_TAINTED  = 1
BLKID_PROBTYPE_PARTNAME = 2
BLKID_PROBTYPE_UNKNOWN  = 3
BLKID_PROBTYPE_LABEL    = 4
BLKID_PROBTYPE_UUID     = 5
BLKID_PROBTYPE_SECTY
