import select
import socket
import sys
import threading
import time
import traceback

import pytest

from . import util
from . import test_base
from . import test_util
from . import test_server
from . import test_client

class TestServer(test_server.TestServer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.server_sock = None
        self.server_thread = None
        self.server_thread_lock = threading.Lock()
        self.server_thread_cond = threading.Condition(self.server_thread_lock)
        self.server_thread_done = False
        self.server_thread_exception = None
        self.server_thread_exception_lock = threading.Lock()
        self.server_thread_exception_cond = threading.Condition(self.server_thread_exception_lock)
        self.server_thread_exception_done = False

    def start(self):
        self.server_sock
