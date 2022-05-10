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

class O(object):
    pass

o = O()
print o
o.__del__ = lambda : print "del"
class A(tuple):
    __slots__ = ()
    def __del__(self):
        print "del A"
        global A
        del A

class B(tuple):
    __slots__ = ()
    def __del__(self):
        print "del B"
        global B
        del B

class C(tuple):
    __slots__ = ()
    def __del__(self):
        print "del C"
        global o
        o += o
        del o

a = A()
b = B()
c = C()
print o

del o
print o
