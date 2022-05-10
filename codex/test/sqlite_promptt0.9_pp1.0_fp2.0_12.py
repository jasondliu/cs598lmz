import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")
import sys
import os
import re
import zipfile
import io
import tempfile
import urllib.request
# python35
# import contextlib
import subprocess

from git import *
# from gitdb.util import hex_to_bin, bin_to_hex, hex_to_base64
# from gitdb.base import IStream
# from gitdb.base import OStream
# from gitdb.util import bin_to_hex
# from gitdb.exc import BadObject
# from gitdb.util import hex_to_bin
# from gitdb.util import hex_to_base64
# from gitdb.exc import BadName
# https://github.com/gitpython-developers/GitPython/issues/302
# from gitdb.db.interface import DB
# import gitdb.db.memory
# import gitdb.util
# import gitdb.exc

import vstruct.defs.git

from vstruct.primitives import *
from vstruct.defs.git import *

from vtrace.const import *
