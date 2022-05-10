import types
types.MethodType(lambda self, x: x, None)

# Test __new__
class C(object):
    def __new__(cls, x):
        return object.__new__(cls)

C(1)

# Test __getattribute__
class D(object):
    def __getattribute__(self, name):
        return 42

D().foo

# Test __getattr__
class E(object):
    def __getattr__(self, name):
        return 42

E().foo

# Test __setattr__
class F(object):
    def __setattr__(self, name, value):
        self.__dict__[name] = value

F().foo = 42

# Test __delattr__
class G(object):
    def __delattr__(self, name):
        del self.__dict__[name]

del G().foo

# Test __get__
class H(object):
    def __get__(self, obj, cls):
        return 42

class I(object):
   
