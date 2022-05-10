import mmap
# Test mmap.mmap(2)
#
# This has only been tested on Linux.
#
# It would be nice to have a more complete test suite.

import os, mmap, struct, time

# Helpers

def assert_raises(exc, fun, *args, **kw):
    try:
        fun(*args, **kw)
    except exc:
        pass
    else:
        print("DID NOT RAISE", exc, fun, args, kw)
        assert 0

def test(expr, expected, comment=""):
    if expr == expected:
        print("ok")
    else:
        print("not ok - %s" % comment)
        print("expected:", expected)
        print("     got:", expr)

# Setup

class mmap_file(object):
    def __init__(self, name, size):
        self.name = name
        f = open(self.name, "w+b")
        f.write(b"\0" * size)
        f.flush()
        f.close()

