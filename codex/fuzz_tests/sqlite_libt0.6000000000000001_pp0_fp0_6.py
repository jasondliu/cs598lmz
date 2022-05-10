import ctypes
import ctypes.util
import threading
import sqlite3
import json
import uuid
import subprocess
import os
import sys
import shutil
import copy
import tempfile
import imp

import xpybutil
import xpybutil.ewmh as ewmh
import xpybutil.util as util
import xpybutil.event as event
import xpybutil.icccm as icccm
import xpybutil.window as window
import xpybutil.root as root
import xpybutil.atom as atom

import xpybutil.compat as compat

# We need to be able to find the pixmaps for the cache, so it needs to be in
# the same directory as the script.
pixmap_dir = os.path.dirname(os.path.realpath(__file__))

# Attempt to find the pixmap cache, by searching the path backwards.
for i in range(1, len(pixmap_dir.split('/'))):
    pixmap_cache = '/'.join(pixmap_dir.split('/')[:-i]) + '/p
