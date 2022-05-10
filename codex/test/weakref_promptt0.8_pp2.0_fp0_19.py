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
