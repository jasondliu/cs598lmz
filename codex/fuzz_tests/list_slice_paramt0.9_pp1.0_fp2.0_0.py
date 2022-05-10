import weakref
class A(object):pass
def callback(x):del lst[0]
keepali0e=[]
lst=[str()]
a=A()
a.c=a
keepali0e.append(weakref.ref(lst,callback))
del a #also collect a
```

```python
class A(object):
    def __init__(self):
        self._observers = []
    def attach(self,observer):
        self._observers.append(observer)
    def notify(self):
        try:
            for o in self._observers:
                o.update()
        except ReferenceError:
            # If the weak reference is invalidated.
            traceback.print_exc()
class Observer(object):
    """
    Interface for updateable objects
    """
    def update(self):
        raise NotImplementedError
class BigBang(object):
    """
    Big bang :P
    """
    def __init__(self,n):
        self.n = n
    def update(self):
        if self.n == 0: raise RuntimeError()
        self.n -= 1
a = A()
o = BigBang(200)
a.attach(weakref.proxy(o))
sys.setrecursionlimit(512)

