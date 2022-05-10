import select
# Test select.select with arguments

def newoff(o, *args):
    try:
        return o.fileno(*args)
    except AttributeError:
        return o

def testargs(o1, o2, o3):
    on = select.select([o1], [o2], [o3], 1)
    assert list(select.select([o1], [o2], [o3], 1, 1.0) == on
               ) == [newoff(obj,'x') for obj in on]


testargs(sys.stdin, sys.stdout, sys.stderr)
testargs(None, sys.stdout, sys.stderr)
testargs(sys.stdin, None, sys.stderr)
testargs(sys.stdin, sys.stdout, None)


import os, random
from test.support import TESTFN, HOST, unlink

# test select() with an invalid file descriptor

filename = TESTFN

f = open(filename, "wb")
n = f.fileno()
try:
    fcntl
