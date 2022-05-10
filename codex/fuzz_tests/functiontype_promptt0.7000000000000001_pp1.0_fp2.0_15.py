import types
# Test types.FunctionType is valid
class A:
    def __init__(self):
        self.f = types.FunctionType(lambda x: x, globals())
    def call(self):
        return self.f(0)

a = A()
assert a.call() == 0

# Test method type is valid
class B:
    def __init__(self):
        self.f = types.FunctionType(lambda x: x, globals(), lambda: None)
    def call(self):
        return self.f(0)

b = B()
assert b.call() == 0
