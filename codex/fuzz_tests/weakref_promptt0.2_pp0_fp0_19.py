import weakref
# Test weakref.ref()
import gc
import sys

class Foo:
    pass

def callback(r):
    print("callback(", r, ")")

def test():
    f = Foo()
    r = weakref.ref(f, callback)
    print("created:", r)
    print("f:", f)
    print("r():", r())
    print("deleting f")
    del f
    print("collecting...")
    gc.collect()
    print("r():", r())
    print("r():", r())
    print("r():", r())
    print("r():", r())
    print("r():", r())
    print("r():", r())
    print("r():", r())
    print("r():", r())
    print("r():", r())
    print("r():", r())
    print("r():", r())
    print("r():", r())
    print("r():", r())
    print("r():", r())
    print("r():", r())
    print("r():
