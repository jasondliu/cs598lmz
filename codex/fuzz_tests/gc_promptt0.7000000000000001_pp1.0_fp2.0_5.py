import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() before and after weakref callback

class C:
    pass

# An instance with a finalizer that returns a list
# which it can modify from the finalizer.
class G:
    def __init__(self):
        self.list = []
        self.wrlist = [weakref.ref(self)]

    def __del__(self):
        self.list.append(1)
        self.wrlist[0]()
        self.list.append(2)

for i in range(5):
    x = G()
    x.list.append(x)
    x.list.append(x)
    x.list.append(x)
    x.list.append(x)
    x.list.append(x)
    x.list.append(x)
    x.list.append(x)
    x.list.append(x)
    x.list.append(x)
    x.list.append(x)
    x.list.append(x)
    x.list.append(x)
    x.list.append
