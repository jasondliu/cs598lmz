import gc, weakref
import sys
import random

class _Mock(object):
    def __init__(self):
        self.foo = 'foo'
        self.bar = lambda: 'bar'
        self.baz = 3.1415
    def __repr__(self):
        return '<_Mock object>'

def _wait_for_gc():
    time.sleep(0.1)
    start = time.time()
    while time.time() < start + 5:
        if gc.collect():
            break
        time.sleep(0.1)

