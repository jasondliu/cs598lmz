import weakref
import time
import threading
import zlib
import os
import sys
import traceback
import platform
import queue
from queue import Queue, Full

if sys.version_info < (3, 0):
    import modules.hglib as pygit
    PY3 = False
else:
    import pygit.hglib as pygit
    PY3 = True

def to_unicode(s):
    if PY3:
        return s
    else:
        return s.decode('utf-8')

def to_bytes(s):
    if PY3:
        return s.encode('utf-8')
    else:
        return s

def get_hg_exe():
    if 'HGEXE' in os.environ:
        return os.environ['HGEXE']
    else:
        if sys.platform == 'win32':
            return 'hg.exe'
        else:
            return 'hg'

