from types import FunctionType
list(FunctionType(lambda: None, globals()))

def f():
    pass

list(FunctionType(f.__code__, globals()))

def f():
    pass

list(FunctionType(f.__code__, globals(), 'f'))

def f():
    pass

list(FunctionType(f.__code__, globals(), 'f', None))

def f():
    pass

list(FunctionType(f.__code__, globals(), 'f', None, None))

def f():
    pass

list(FunctionType(f.__code__, globals(), 'f', None, None, None))

def f():
    pass

list(FunctionType(f.__code__, globals(), 'f', None, None, None, None))

def f():
    pass

list(FunctionType(f.__code__, globals(), 'f', None, None, None, None, None))

def f():
    pass

list(FunctionType(f.__code__, globals(), 'f', None,
