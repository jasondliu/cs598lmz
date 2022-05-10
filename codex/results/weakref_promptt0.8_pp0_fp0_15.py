import weakref
# Test weakref.ref(subclass_of_weakref) and weakref.proxy(subclass_of_weakref)

import sys
import weakref
try:
    import _weakref
except ImportError:
    _weakref = None

class X:
    pass

class Weak(weakref.ref, X):
    pass

if sys.platform != "win32":
    class WeakProxy(weakref.proxy, X):
        pass

# Create a function to fake a reference cycle with:
#   C1 --> C2 --> C3 --> C4 --\
#                               \--> C5 --> C6 ---\
#   C7 --------------------------------------------/

def create_cycle():
    global C1, C2, C3, C4, C5, C6, C7

    class C1:
        def __init__(self):
            self.c2 = C2()

    class C2:
        def __init__(self):
            self.c3 = C3()

    class C3:
        def __init__(self):
            self.c4 = C
