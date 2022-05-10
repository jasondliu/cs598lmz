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
del latefin
```

```
(Pdb) gc.collect()
1
(Pdb) gc.collect()
0
(Pdb) gc.collect()
0
(Pdb) n
> <doctest test.test_descr.test_module.__del__[1]>(28)__del__()
-> self[1].ref = weakref.ref(self[0])
(Pdb) self
<__main__.Cyclic object at 0x0000000005618198>
(Pdb) self[1]
<__main__.LateFin object at 0x0000000005618208>
(Pdb) self[1].ref = weakref.ref(self[0])
(Pdb) n
> <doctest test.test_descr.test_module.__del__[1]>(29)__del__()
-> global latefin
(Pdb) self[1].ref
<weakref at 0x0000000005618308; to 'function' at 0x0000000005618128
