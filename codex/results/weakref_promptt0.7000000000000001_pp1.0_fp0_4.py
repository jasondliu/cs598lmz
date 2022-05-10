import weakref
# Test weakref.ref()
import gc

def callback(arg):
    print "Callback called:", arg

class Test:
    def __init__(self):
        self.ref = weakref.ref(self, callback)
        self.x = 42
        self.a = self # cycle

    def __del__(self):
        print "Test.__del__()"

def main():
    try:
        obj = Test()
    except TypeError, err:
        print err
        return

    if callback.__self__ is not None:
        raise TestFailed("callback should not be bound to an object")

    if obj.ref() is not obj:
        raise TestFailed("ref returned was not obj")

    del obj

    gc.collect()

    if callback.__self__ is not None:
        raise TestFailed("callback should not be bound to an object")

    print "All OK"

main()
