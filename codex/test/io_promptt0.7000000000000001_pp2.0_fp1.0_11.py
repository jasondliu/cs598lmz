import io
# Test io.RawIOBase
try:
    io.RawIOBase.name
    io.RawIOBase.isatty
    io.RawIOBase.fileno
except AttributeError:
    print("SKIP")
    raise SystemExit

import sys

class TestRawIO(io.RawIOBase):
    def write(self, b):
        sys.stdout.write(b)

TestRawIO().write(b"foo")

# Issue #3613: test that RawIOBase objects are not iterable
try:
    iter(TestRawIO())
    raise Exception("TypeError not raised")
except TypeError:
    print("TypeError")

# Test invalid args
try:
    io.RawIOBase()
except TypeError:
    print("TypeError")

try:
    io.RawIOBase().read1()
except NotImplementedError:
    print('NotImplementedError')

try:
    io.RawIOBase().readinto1()
except NotImplementedError:
    print('NotImplementedError')
