import select
import signal
import sys
import thread
import threading
import time
import traceback

from cStringIO import StringIO

from mwlib.log import Log

log = Log("mwlib.server")

# Used in testing:
_testing = False

# Used in recording
_recorder = None

def _getRecorder():
    global _recorder
    if not _recorder:
        _recorder = _Recorder()
    return _recorder

def record(cmd):
    """Used in testing _Recorder."""
    return _getRecorder().record(cmd)

def replay():
    """Used in testing _Recorder."""
    return _getRecorder().replay()

def setUp():
    """Used in testing _Recorder."""
    global _recorder
    _recorder = _Recorder()
    
def tearDown():
    """Used in testing _Recorder."""
    global _recorder
    _recorder = None

