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

# The following is a workaround for a bug in Python 2.6.
# See http://bugs.python.org/issue4184 for details.
# This is not needed in Python 2.7.
import sys
if sys.version_info[:2] == (2, 6):
    import gc
    gc.collect()

# The following is a workaround for a bug in Python 2.7.
# See http://bugs.python.org/issue4184 for details.
# This is not needed in Python 2.7.
import sys
if sys.version_info[:2] == (2, 7):
    import gc
    gc.collect()

# The following is a workaround for a bug in Python 2.7.
# See http://bugs.python.org/issue4184 for details.
# This is not needed in Python 2.7.
import sys
if sys.version_info[:2] == (2, 7):
    import gc
    gc.collect()

# The following is a workaround for a bug in Python 2
