import types
# Test types.FunctionType
def f(): pass
raise isinstance(f, types.FunctionType)

def f(a, b, c): pass
raise isinstance(f, types.FunctionType)

def f(a, b, c=1): pass
raise isinstance(f, types.FunctionType)

def f(a, b, c=1, *args): pass
raise isinstance(f, types.FunctionType)

def f(a, b, c=1, *args, **kwds): pass
raise isinstance(f, types.FunctionType)

def f(a, b, c=1, d=2, *args, **kwds): pass
raise isinstance(f, types.FunctionType)

def f(a, b, c=1, d=2, **kwds): pass
raise isinstance(f, types.FunctionType)

def f(a, b, *, c): pass
raise isinstance(f, types.FunctionType)

def f(a, b, *, c, **kwds): pass
raise isinstance(f, types.FunctionType
