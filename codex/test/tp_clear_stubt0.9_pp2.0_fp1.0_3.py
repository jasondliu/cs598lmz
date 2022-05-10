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
# Uncomment next line to set the reference used in weakref.proxycall
# latefin

import tempfile
import os

thefile = tempfile.NamedTemporaryFile()

def remove_the_file():
    os.remove(thefile.name)
thefile.close()

class TemporyFileProxy:
    __slots__ = 'name', 'origin'

    def __init__(self):
        self.origin = thefile
        self.name = self.origin.name

    def __repr__(self):
        return '<%s name=%r>' % (self.__class__.__name__, self.name)
    def __del__(self):
        self.origin.close()
        del self.origin

proxy = TemporyFileProxy()

import proxycall

if proxycall.test(remove_the_file, proxy, os.path.exists, thefile.name, wargs=(proxy,)):
    raise TestFailed("Failed static method test.")


proxy.origin = testcap
