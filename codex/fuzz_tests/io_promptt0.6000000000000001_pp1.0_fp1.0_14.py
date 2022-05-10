import io
# Test io.RawIOBase with a socket

import socket
import unittest
import threading


class SocketReadingTest(unittest.TestCase):
    def test_read_into(self):
        # This test is Linux-specific.
        s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        s.connect(b"/dev/log")
        s.setblocking(False)

        buf = bytearray(10)
        with self.assertRaises(BlockingIOError):
            s.readinto(buf)
        self.assertEqual(s.readinto(buf), 0)

        buf = bytearray(10)
        s.setblocking(True)
        s.send(b"Hello")
        self.assertEqual(s.readinto(buf), 5)
        self.assertEqual(buf, b"Hello\0\0\0\0\0")


class SocketWritingTest(unittest.TestCase):
    def test_write(self):
        # This test is Linux-specific.
        s =
