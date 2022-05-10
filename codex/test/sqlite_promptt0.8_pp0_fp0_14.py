import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect with a URI that has a hostname
# and a password.
#
test.test_support.verbose = 1
# If the _sqlite module is shared, the test cannot run twice in the same
# interpreter process.
#
test.test_support.reap_children = 1

db_base = test.test_support.TESTFN

# This is used to lock the thread running the server.
thread_running = threading.Event()

class HelperServer(object):

    def __init__(self):
        self.lock = threading.Lock()
        self.cond = threading.Condition(self.lock)

    def serve_forever(self):
        import time
        import BaseHTTPServer

        class Handler(BaseHTTPServer.BaseHTTPRequestHandler):

            def do_GET(self):
                self.send_response(200)
                self.end_headers()
                self.wfile.write('Hello, world!')
                with self.server.lock:
                    self.server.cond.notify()

        # Serve until the calling test thread
