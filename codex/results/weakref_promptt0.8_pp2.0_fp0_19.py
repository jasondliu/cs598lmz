import weakref
# Test weakref.ref()
import _weakref

class G:
    pass

class H(G):
    pass

def foo():
    return G()

def bar():
    return H()

w = weakref.ref(foo())
print type(w)
print w() is None
print w() is foo()
print weakref.ref(foo())
print weakref.getweakrefcount(foo())
print weakref.getweakrefs(foo())
w = None
print weakref.getweakrefcount(foo())
print weakref.getweakrefs(foo())

w = weakref.ref(foo())
print weakref.getweakrefcount(foo())
print weakref.getweakrefs(foo())
print w() is None
w = None
print weakref.getweakrefcount(foo())
print weakref.getweakrefs(foo())

w = weakref.ref(foo(), lambda _: print("dead"))
print weakref.getweakrefcount(foo())
print weakref.getweakrefs(foo())
del foo
print weakref.get
