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

func()

# This should cause a deadlock between the garbage collector
# and the Python thread state lock.
import gc,time,threading

class A:
    def __del__(self):
        gc.collect()

def f():
    while True:
        time.sleep(0)

a = A()
threading.Thread(target=f).start()

# This should crash the interpreter
import gc

def f(arg):
    if arg:
        f(arg-1)
    class X:
        def __del__(self):
            f(True)
    X()

for i in range(2000):
    gc.collect()

f(10)

# This should crash the interpreter (if the registry doesn't protect itself)
import gc

class S:
    pass

def f():
    class X:
        def __del__(self):
            gc.collect()
    X()

s = S()
s.f = f
s.f()

#
