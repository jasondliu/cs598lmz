import ctypes
import ctypes.util
import threading
import sqlite3 as sqlite
import base64

class SmartCache:
    """fast thread-safe caching of CPU-expensive python methods.

    This class provides a smart mechanism for caching functions that
    return an expensive value (commonly: a result from a CPU-expensive
    parsing algorithm).  The key cache parameter is a raw hashing
    table that is shared across threads, and the cache can detect if
    two threads are trying to compute the same cached value.

    As an added bonus, the cache improves the efficiency of multithreaded
    matlab computation.  I have noticed huge efficiency improvements when
    generating large numbers of cached values in multithreaded matlab
    computation.

    Basic usage:

    class Foo(SmartCache):
        def __init__(self, a, b):
            SmartCache.__init__(self)
            self.a = a
            self.b = b
        def computeFoo(self):
            self.cached('foo', self.a + self.b)

    f = Foo(1, 2)
    f.computeFoo() ### Cached calculation
    f.foo        
