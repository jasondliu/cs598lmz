import weakref
# Test weakref.ref() with callbacks

class Foo(object):
    pass

def callback(w):
    global n
    n -= 1
