import types
# Test types.FunctionType

def func():
    pass

def func1():
    pass

class A:
    def func2(self):
        pass

class B(A):
    def func3(self):
        pass

class C(B):
    def func4(self):
        pass

a = A()
b = B()
c = C()

# Test FunctionType
assert type(func) == types.FunctionType
assert type(func1) == types.FunctionType
assert type(a.func2) == types.MethodType
assert type(b.func3) == types.MethodType
assert type(c.func4) == types.MethodType

# Test FunctionType.__name__
assert func.__name__ == 'func'
assert func1.__name__ == 'func1'
assert a.func2.__name__ == 'func2'
assert b.func3.__name__ == 'func3'
assert c.func4.__name__ == 'func4'

# Test FunctionType.__qualname__
assert func.__qualname__ ==
