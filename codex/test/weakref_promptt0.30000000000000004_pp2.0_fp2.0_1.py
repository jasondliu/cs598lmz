import weakref
# Test weakref.ref() with a class that has a __del__ method.

class C:
    def __del__(self):
        pass

def callback(r):
    print("callback called")

r = weakref.ref(C(), callback)
del r
