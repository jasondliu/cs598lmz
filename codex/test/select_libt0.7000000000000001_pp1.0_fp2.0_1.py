import selectors
import sys
import time
import utils

EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
SERVER_HOST = 'localhost'
SERVER_PORT = 8888
REQUEST_QUEUE_SIZE = 5


class Future:
    def __init__(self):
        self.result = None
        self._callbacks = []

    def add_done_callback(self, fn):
        self._callbacks.append(fn)

    def set_result(self, result):
        self.result = result
        for fn in self._callbacks:
            fn(self)

    def __iter__(self):
        yield self
        return self.result


class Task:
    def __init__(self, coro):
        self.coro = coro
        f = Future()
        f.set_result(None)
        self.step(f)

