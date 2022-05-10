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
del view

gc.collect()
assert len(gc.garbage) == 1
assert gc.garbage[0] is File
assert weakref.getweakrefcount(File) == 0

gc.collect()
assert len(gc.garbage) == 1
assert gc.garbage[0] is File
gc.garbage.pop()

# Issue 3001
#
# If a cycle is broken and an instance with a __del__ is still alive
# because it's part of a cycle, then when the cycle is broken, it should
# still have a __del__ and finalization should work correctly.

class Final:
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return 'Final: %s' % self.val
    def __repr__(self):
        return '<Final: %s>' % self.val
    def __del__(self):
        print('Final.__del__', self)

class StillAlive:
    def __init__(self):
        self.a
