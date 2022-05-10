import types
# Test types.FunctionType()

def test_functiontype_0():
    '''
    Test FunctionType(code, globals, name, defaults, closure) with
    all keyword arguments provided.
    '''
    def f(x, y=1, *args, **kwargs):
        pass

    assert type(types.FunctionType(f.__code__,
                                   f.__globals__,
                                   f.__name__,
                                   f.__defaults__,
                                   f.__closure__)) is types.FunctionType

def test_functiontype_1():
    '''
    Test FunctionType(code, globals, name, defaults, closure) with
    only the required arguments provided.
    '''
    def f(x, y=1, *args, **kwargs):
        pass

    assert type(types.FunctionType(f.__code__,
                                   f.__globals__,
                                   f.__name__)) is types.FunctionType

def test_functiontype_2():
    '''
    Test FunctionType(code, globals
