import weakref
# Test weakref.ref() on a class with a __del__ method

class C(object):
    def __init__(self):
        self.x = 1
    def __del__(self):
        pass

obj = C()

def f():
    obj.x

r = weakref.ref(obj, f)

del obj

print(r())

del r

import gc
gc.collect()
