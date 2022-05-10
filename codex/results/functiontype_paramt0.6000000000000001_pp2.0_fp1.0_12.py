from types import FunctionType
list(FunctionType(FunctionType.__code__, globals(), 'foo')())

# noinspection PyUnusedLocal,PyUnresolvedReferences
def foo():
    for i in range(100):
        yield i

list(FunctionType(FunctionType.__code__, globals(), 'foo')())

# noinspection PyUnusedLocal,PyUnresolvedReferences
def bar():
    for i in range(100):
        yield i

list(FunctionType(FunctionType.__code__, globals(), 'bar')())

# noinspection PyUnusedLocal,PyUnresolvedReferences
def bar():
    for i in range(100):
        yield i

list(FunctionType(FunctionType.__code__, globals(), 'bar')())

# noinspection PyUnusedLocal,PyUnresolvedReferences
def bar():
    for i in range(100):
        yield i

list(FunctionType(FunctionType.__code__, globals(), 'bar')())

# noinspection PyUnusedLocal,PyUnresolvedReferences
def bar():
    for i in
