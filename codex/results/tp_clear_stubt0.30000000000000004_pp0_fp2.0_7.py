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

# The following line should not crash.
del latefin
```

### [PYTHON-1558](https://issues.apache.org/jira/browse/PYTHON-1558) - `__del__` method of `weakref.ref` objects should not be called when the object is garbage collected

```python
import gc, weakref

class A:
    def __del__(self):
        print('A.__del__')

a = A()
r = weakref.ref(a)
del a
gc.collect()

# The following line should not print 'A.__del__'.
del r
```

### [PYTHON-1559](https://issues.apache.org/jira/browse/PYTHON-1559) - `__del__` method of `weakref.ref` objects should not be called when the object is garbage collected

```python
import gc, weakref

class A:
    def __del__(self):
        print('A.
