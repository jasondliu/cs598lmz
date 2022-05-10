import io
# Test io.RawIOBase on Windows to ensure that non-inheriting descendants can
# be used as raw I/O.
# On Windows, all modules that depend on the _winapi module should be imported
# before importing the _multiprocessing module.
from multiprocessing.dummy import Pool
from tkinter import *
import os, sys
import time
from subprocess import *
from io import StringIO
if os.path.exists(os.getcwd() + '\\operations\\www.py') and os.path.exists(os.getcwd() + '\\modules\\www.py'):
    if os.path.exists(os.getcwd() + '\\operations\\req.py') and os.path.exists(os.getcwd() + '\\modules\\req.py'):
        import www, req
    else:
        import www
        req = False
else:
    www = False
    import req

def stop_logger(l):
    from queue import Empty
    if sys.version_info[0] < 3:
        while 1
