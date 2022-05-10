import types
# Test types.FunctionType
class A:
    def foo(self):
        pass

class B(A):
    pass

def bar():
    pass

def foo():
    pass

try:
    types.FunctionType(A.foo, globals())
except TypeError:
    print('TypeError')

try:
    types.FunctionType(A.foo)
except TypeError:
    print('TypeError')

try:
    types.FunctionType(A.foo, 0)
except TypeError:
    print('TypeError')

try:
    types.FunctionType(A.foo, globals(), B.foo)
except TypeError:
    print('TypeError')

try:
    types.FunctionType(A.foo, globals(), 0)
except TypeError:
    print('TypeError')

try:
    types.FunctionType(A.foo, globals(), **{0: 'foo'})
except TypeError:
    print('TypeError')

try:
    types.FunctionType(A.foo, globals(), **{'foo': 'foo
