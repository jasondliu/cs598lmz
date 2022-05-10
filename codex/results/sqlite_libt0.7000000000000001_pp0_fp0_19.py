import ctypes
import ctypes.util
import threading
import sqlite3 as sqlite
import time
import logging

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


def log_error():
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    log.addHandler(logging.StreamHandler())


class DummyFile(object):
    def write(self, x):
        pass


@contextmanager
def nostderr():
    save_stderr = sys.stderr
    sys.stderr = DummyFile()
    yield
    sys.stderr = save_stderr


class WebSocketThread(threading.Thread):
    def __init__(self, ip, port):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.chat_id = None

    def run(self):
        chat_id = self.chat_id
        self.app = Flask(__name__)
        self.app.config['SEC
