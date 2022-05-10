import select
import socket
import sys
import time
import traceback
import threading

try:
    from queue import Queue
except ImportError:  # Python 2.x
    from Queue import Queue

def _print_exc(exc):
    try:
        print(exc)
        traceback.print_exc()
    except IOError:
        pass

class _Server(object):
    def __init__(self, options):
        self._options = options
        self._socket = None
        self._thread = None
        self._queue = Queue()
        self._closed = False

    def _run(self):
        while not self._closed:
            try:
                self._run_once()
            except KeyboardInterrupt:
                break
            except Exception as exc:
                _print_exc(exc)

    def _run_once(self):
        sock = self._socket
        if sock is None:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
