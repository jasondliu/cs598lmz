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
del func, cyc, LateFin

for i in range(1024):
    print(gc.collect())
</code>
Output under Python 3.7.2:
<code>0
12
10
0
0
0
...
</code>
Output under Python 3.8a0:
<code>0
0
12
10
0
0
...
</code>
In other words, the first call to <code>gc.collect()</code> in Python 3.8 collects 12 unreachable objects as expected, but the subsequent calls only collect 10 at a time. If I run your code in Python 3.8, I get:
<code>0
0
15
13
10
11
0
0
0
</code>
which seems a bit random to me.

