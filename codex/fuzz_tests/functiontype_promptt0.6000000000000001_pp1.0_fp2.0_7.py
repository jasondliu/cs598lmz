import types
# Test types.FunctionType
def f(): pass
f.__code__ = types.CodeType(0, 0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')
f.__code__.co_argcount = 7
f()

# Test types.MethodType
def g(): pass
g.__code__ = types.CodeType(0, 0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')
g.__code__.co_argcount = 7
class C:
    method = types.MethodType(g, None)

C().method()

# Test types.LambdaType
def h(): pass
h.__code__ = types.CodeType(0, 0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')
h.__code__.co_argcount = 7
l = types.LambdaType(h, {})
l()

# Test types.GeneratorType
def i():
    yield 1
i.gi_frame = lambda: None
i
