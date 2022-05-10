import types
# Test types.FunctionType
@types.FunctionType
def foo():
    pass

@types.FunctionType
def bar(a, b):
    pass

@types.FunctionType
def bar(a, b, *args):
    pass

@types.FunctionType
def bar(a, b, *args, **kwargs):
    pass

@types.FunctionType
def bar(a, b, *args, c):
    pass

@types.FunctionType
def bar(a, b, *args, c, **kwargs):
    pass

@types.FunctionType
def bar(a, b, *, c):
    pass

@types.FunctionType
def bar(a, b, *, c, **kwargs):
    pass

@types.FunctionType
def bar(a, b=None):
    pass

@types.FunctionType
def bar(a, b=None, *args):
    pass

@types.FunctionType
def bar(a, b=None, *args, **kwargs):
    pass

@types.FunctionType
def bar
