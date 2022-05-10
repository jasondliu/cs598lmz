import ctypes
import ctypes.util
import threading
import sqlite3
import datetime

logger = logging.getLogger(__name__)

if sys.platform == 'darwin':
    import CF

# Complements Utilities
# Only daemon threads are killed when 'killall python' is issued.
def kill_daemon_threads(signal=None, frame=None):
    current_thread = threading.current_thread()
    for thread in threading.enumerate():
        if thread is current_thread:
            continue
        if not thread.isDaemon():
            continue
        logger.warning('Killing LiveThread: {0}'.format(thread.name))
        try:
            exc = ctypes.py_object(SystemExit)
            res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(thread.ident), exc)
            if res == 0:
                raise ValueError('nonexistent thread id')
            elif res > 1:
                # 'if it returns a number greater than one, you're in trouble,
                # and you should call it again with exc=NULL to
