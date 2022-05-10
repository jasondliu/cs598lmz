import gc, weakref

class LateFin:
    __slots__ = ('ref',)
    def __del__(self):
        global func
        func = self.ref()

class Cyclic(tuple):
    __slots__ = ()
    def __del__(self):
        self[1].ref = weakref.ref(self[0])
        global latefin
        del latefin

latefin = LateFin()
func = lambda: None
cyc = tuple.__new__(Cyclic, (func, latefin))

func.__module__ = cyc
del func, cyc
gc.collect()

import os
import sys

def main(script):
    if '__pypy__' in sys.builtin_module_names:
        # PyPy does not support the C API for set_inheritable.
        # Also, the fd is likely to be closed anyway due to the
        # _io module.
        return
    # This part of the test is not run in PyPy because we don't
    # have a C implementation of set_inheritable().  It is also
    # not run in Python 3.3 and above because of the change in
    # the implementation of os.dup() (see issue14792).
    fd = os.open(script, os.O_RDONLY)
    sys.stdin = os.fdopen(fd)
    os.set_inheritable(fd, True)
    os.close(fd)
    # This part is skipped in PyPy because of the lack of a C
    # implementation of set_inheritable().
    if sys.platform.startswith('win'):
        sys
