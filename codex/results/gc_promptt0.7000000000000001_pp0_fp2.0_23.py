import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with weakref callbacks
class MyRef(weakref.ref):
    def __init__(self):
        self.callback = lambda: None
    def __call__(self):
        self.callback()
        return super(MyRef, self).__call__()

def callback():
    print("callback")

def callback2():
    print("callback2")

def test():
    a = MyRef()
    a.callback = callback
    b = MyRef()
    b.callback = callback2
    objs = [a, b]
    del a, b
    gc.collect()
    print(objs)

test()
