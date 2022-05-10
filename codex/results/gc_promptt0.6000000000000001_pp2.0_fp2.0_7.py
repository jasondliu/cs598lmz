import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with callback

class ObjectWithFinalizer:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print('del:', self.name)

def callback(ref):
    print("callback", ref)

def main():
    # Create some objects
    for i in range(10):
        ObjectWithFinalizer("Object %d" % i)

    # Collect them
    gc.collect()
    # Create some more objects
    for i in range(10):
        ObjectWithFinalizer("Object %d" % i)
    gc.collect()

    # Create some cyclic objects
    a = ObjectWithFinalizer("Object A")
    b = ObjectWithFinalizer("Object B")
    a.other = b
    b.other = a

    # Collect one of them
    gc.collect()

    # Create some cyclic objects with finalizers
    a = ObjectWithFinalizer("Object A")
    b = ObjectWithFinalizer("Object B")
    a.other = b
    b.other =
