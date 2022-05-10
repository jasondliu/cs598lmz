import select
# Test select.select() with large buffersize
# Note that this test fails if select() does not support large buffers

import subprocess
import threading
import time

import _testcapi

def start_server(server_socket):
    # Common code for server processes
    def read_all(sock):
        data = ''
