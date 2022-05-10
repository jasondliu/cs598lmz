import weakref
# Test weakref.ref()
class C(object):
    pass

weakref.ref(C)
weakref.ref(C())

# Test weakref.ref(callable)
weakref.ref(len)

# Test weakref.ref(function)
def f(): pass
weakref.ref(f)

# Test weakref.ref(classmethod)
class D(object):
    @classmethod
    def cm(cls): pass
weakref.ref(D.cm)

# Test weakref.ref(staticmethod)
class E(object):
    @staticmethod
    def sm(): pass
weakref.ref(E.sm)

# Test weakref.ref(class)
weakref.ref(future)

# Test weakref.ref(type)
weakref.ref(type)

# Test weakref.ref(exception)
weakref.ref(KeyError)

# Test weakref.ref(dict)
d = {}
weakref.ref(d)

# Test weakref.ref(list)
l = []
weakref.ref(
