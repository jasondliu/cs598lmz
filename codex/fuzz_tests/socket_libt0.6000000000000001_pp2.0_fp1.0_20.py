import socket
import struct
import threading
import time
import traceback

from . import lib
from . import log


class Client:
    def __init__(self, host, port, timeout=3):
        self._host = host
        self._port = port
        self._timeout = timeout

    def send(self, data, *, timeout=None):
        if not timeout:
            timeout = self._timeout
        else:
            timeout /= 1000

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        try:
            sock.connect((self._host, self._port))
            sock.sendall(data)
        except Exception:
            log.error(traceback.format_exc())
            return False
        finally:
            sock.close()
        return True


class Server:
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._sock = None
        self._running = False

    def start(self):
