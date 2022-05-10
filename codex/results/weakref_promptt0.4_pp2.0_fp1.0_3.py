import weakref
# Test weakref.ref() on a class instance.

class C(object):
    pass

o = C()
r = weakref.ref(o)

print r() is o

del o
print r() is None

# Test weakref.ref() on a class instance with a __del__ method.

class D(object):
    def __del__(self):
        print "del"

o = D()
r = weakref.ref(o)

print r() is o

del o
print r() is None

# Test weakref.ref() on a class instance with a __del__ method that raises an
# exception.

class E(object):
    def __del__(self):
        raise Exception

o = E()
r = weakref.ref(o)

print r() is o

del o
print r() is None

# Test weakref.ref() on a class instance with a __del__ method that raises an
# exception that is caught.

class F(object):
    def __del__(self):
        try:
            raise
