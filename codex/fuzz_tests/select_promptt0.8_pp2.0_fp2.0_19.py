import select
# Test select.select() and select.poll()

import errno

import unittest
from test import support
if not hasattr(select, 'poll'):
    raise unittest.SkipTest('poll not defined')

class TestSelect(unittest.TestCase):

    def setUp(self):
        self.read_fd, self.write_fd = os.pipe()

    def tearDown(self):
        os.close(self.read_fd)
        os.close(self.write_fd)

    def pollster(self, timeout, expected_events):
        poll_obj = select.poll()
        poll_obj.register(self.read_fd, select.POLLIN)
        timeout_in_millis = int(timeout * 1000)
        events = poll_obj.poll(timeout_in_millis)
        self.assertEqual(events, expected_events)

    def test_poll(self):
        for i in range(5):
            os.write(self.write_fd, b"x")
        self.pollster(0, [(self.
