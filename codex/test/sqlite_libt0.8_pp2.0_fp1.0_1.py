import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import os
import struct

# constants used to select the source/sink
SOURCE_FILE = 1
SOURCE_BUFFER = 2
SINK_FILE = 1
SINK_BUFFER = 2

# constants used to construct the status flags
STATUS_UPDATED = 1
STATUS_END = 2


class _StreamPipeline(ctypes.Structure):
    """
    A C structure containing pointers to the various functions
    required to implement a plugin.
    """
