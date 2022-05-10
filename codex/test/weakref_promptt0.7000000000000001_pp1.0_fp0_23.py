import weakref
# Test weakref.ref()

class Foo(object):

    def __init__(self):
        self.refs = []
        for i in range(3):
            self.refs.append(weakref.ref(self))


    def __del__(self):
        pass

f = Foo()
del f
import gc
gc.collect()
