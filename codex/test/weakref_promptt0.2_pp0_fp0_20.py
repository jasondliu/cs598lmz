import weakref
# Test weakref.ref() with a class that has a __del__ method.

class C:
    def __del__(self):
        pass

def f():
    c = C()
    r = weakref.ref(c)
    del c
    return r

r = f()
print(r())

# Test weakref.ref() with a class that has a __del__ method that raises an
# exception.

class C:
    def __del__(self):
        raise Exception

def f():
    c = C()
    r = weakref.ref(c)
    del c
    return r

r = f()
print(r())

# Test weakref.ref() with a class that has a __del__ method that raises an
# exception that is caught.

class C:
    def __del__(self):
        try:
            raise Exception
        except:
            pass

def f():
    c = C()
    r = weakref.ref(c)
    del c
    return r

r = f()
print(r())

