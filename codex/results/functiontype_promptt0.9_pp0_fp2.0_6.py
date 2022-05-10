import types
# Test types.FunctionType
class A:
    pass
def f():
    return 0
f.__name__
type(f)
type(A)
type(f) == type(lambda: None)
type(f) == types.FunctionType
type(f) == type
# Test types.UnboundMethodType
class A:
    def f():
        return 0
f = A.f
type(f) == types.UnboundMethodType
# Test types.MethodType
class A:
    def f():
        return 0
f = A.f.__get__(1, A)
type(f) == types.MethodType
# Test types.LambdaType
f = lambda x: x+0
type(f) == types.LambdaType
a = object()

exec(
"""if 1:
    def f(): return 2
else:
    def g(): return 3
""")
type(f) == types.FunctionType
type(a.__class__.__repr__)
type(type)
type(None)
type(str)
type(len)
type
