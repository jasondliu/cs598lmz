import mmap
import os
import sys
import tempfile
import thread
import threading
import time
import unittest

import server


class TestCase(unittest.TestCase):
    def setUp(self):
        self.server_thread = threading.Thread(target=server.main)
        self.server_thread.start()

    def tearDown(self):
        time.sleep(1)
        pid = int(open('/tmp/server.pid').read())
        os.kill(pid, 15)
        self.server_thread.join()

    def test_initial_config(self):
        self.assertEqual(
            {'config': {'port': 8080, 'secret': 'foo'}},
            self.get('/config'))

    def test_change_config(self):
        self.assertEqual(
            {'status': 'ok'},
            self.post('/config', {'secret': 'bar'}))
        self.assertEqual(
            {'config': {'port': 8080, 'secret': 'bar
