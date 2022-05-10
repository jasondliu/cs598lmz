import types
# Test types.FunctionType()
func1 = lambda x, y, z: x + y + z
func2 = types.FunctionType(func1.__code__, globals())
print(func2(2, 3, 4))
"""
types.FunctionType(code, globals[, name[, argdefs[, closure]]])
Return a new function object from a code object and a dictionary.

The optional name string overrides the name from the code object. The optional argdefs tuple specifies the default argument values. The optional closure tuple supplies the bindings for free variables.
"""

print()

# test types.MethodType()
class A:
    def __init__(self, name):
        self.name = name
    def foo(self):
        print('my name is', self.name)

a = A('abc')
# MethodType() 相当于给某个类的方法赋值，比如下面的a.bar = foo
a.bar = types.MethodType(a.foo,
