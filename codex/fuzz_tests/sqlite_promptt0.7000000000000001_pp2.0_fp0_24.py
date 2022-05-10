import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')
import sys
import os
import time
import re
import subprocess
import traceback
import signal
import errno
import json
import datetime
# import fcntl
import struct
import termios
import glob
import contextlib

# test_sqlite3 = True
test_sqlite3 = False
test_sqlite3_prepare_v2 = False
test_sqlite3_prepare_v2_0 = False
test_sqlite3_prepare_v2_1 = False
test_sqlite3_prepare_v2_2 = False
test_sqlite3_prepare_v2_3 = False
test_sqlite3_prepare_v2_4 = False
test_sqlite3_prepare_v2_5 = False

test_sqlite3_step_v2 = False
test_sqlite3_step_v2_0 = False
test_sqlite3_step_v2_1 = False
test_sqlite3_step_v2_2 = False
test_sqlite3_step
