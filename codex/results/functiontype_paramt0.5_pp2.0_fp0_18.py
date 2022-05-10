from types import FunctionType
list(FunctionType(
    FunctionType.__code__,
    FunctionType.__globals__,
    'test',
    FunctionType.__defaults__,
    FunctionType.__closure__
))

# code_object
import types

def fn():
    pass

code_object = types.CodeType(
    0,
    0,
    0,
    0,
    b'',
    (),
    (),
    (),
    '',
    '',
    0,
    b''
)

# 用type创建类
def fn(self):
    pass

Foo = type('Foo', (object,), dict(fn=fn))

# 用type创建类
def fn(self):
    pass

Foo = type('Foo', (object,), dict(fn=fn))

# 用type创建类
def fn(self):
    pass

Foo = type('Foo', (object,), dict(fn=fn))


