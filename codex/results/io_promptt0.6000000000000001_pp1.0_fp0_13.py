import io
# Test io.RawIOBase.read()

import _io

# Testing RawIOBase.read()

class TestRawIO(io.RawIOBase):

    def __init__(self, test_dict):
        self.read_stack = test_dict['read_stack']
        self.read_stack.reverse()
        self.read_count = 0
        self.read_history = []

    def readable(self):
        return True

    def readinto(self, b):
        s = self.read_stack.pop()
        n = len(s)
        self.read_history.append((n, b[:n]))
        b[:n] = s
        self.read_count += 1
        return n

    def read(self, n=-1):
        s = self.read_stack.pop()
        self.read_history.append((n, s[:n]))
        self.read_count += 1
        return s[:n]

# Readline tests

class TestRawIO(io.RawIOBase):

    def __init__(self,
