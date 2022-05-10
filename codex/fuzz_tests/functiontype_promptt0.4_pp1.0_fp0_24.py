import types
# Test types.FunctionType
def test_function_type():
    def func():
        pass
    assert isinstance(func, types.FunctionType)
    # Test __name__
    assert func.__name__ == 'func'
    # Test __doc__
    assert func.__doc__ == None
    # Test __dict__
    assert func.__dict__ == {}
    # Test __defaults__
    assert func.__defaults__ == None
    # Test __code__
    assert isinstance(func.__code__, types.CodeType)
    # Test __globals__
    assert func.__globals__ == {}
    # Test __closure__
    assert func.__closure__ == None
    # Test __module__
    assert func.__module__ == '__main__'
    # Test __annotations__
    assert func.__annotations__ == {}
    # Test __kwdefaults__
    assert func.__kwdefaults__ == None
    # Test __get__
    assert func.__get__(None, object) == func
    # Test __call__
   
