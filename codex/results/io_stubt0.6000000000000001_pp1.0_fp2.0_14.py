import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

# Issue #10126: Test that objects with a destructor are not finalized
# before their __del__ method runs.
class Spam(object):
    def __del__(self):
        self.ran = True

import weakref
s = Spam()
r = weakref.ref(s)
del s
gc.collect()
assert r() is not None
del r
gc.collect()
assert Spam.__del__.__self__.ran

# Issue #10131: Test that cyclic gc doesn't crash in debug mode
class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def create_tree(depth):
    if depth <= 0:
        return Node(None)
    else:
        return Node(
            depth,
            create_tree(depth - 1),
            create_tree(depth - 1))

root = create_tree(10)
gc.collect()

# Issue #10194: test
