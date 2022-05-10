import types
# Test types.FunctionType

# Test __new__

class A(object):
    def __new__(cls):
        def f():
            pass
        return f

a = A()
print a, type(a)

# Test __get__

class B(object):
    def __init__(self):
        self.f = types.FunctionType(self.f.func_code, self.f.func_globals)
    def __get__(self, obj, cls):
        return self.f
    def f():
        pass

b = B()
print b, type(b)

print b.__get__(None, None), type(b.__get__(None, None))
