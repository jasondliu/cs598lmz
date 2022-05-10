import types
# Test types.FunctionType

def test_function_type_callable_1():
    def foo():
        pass

    assert types.FunctionType(foo.__code__, globals())() is None

def test_function_type_callable_2():
    def foo(a):
        pass

    assert types.FunctionType(foo.__code__, globals(), "foo",
                              ("a",), None)(1) is None

def test_function_type_callable_3():
    def foo(a, b):
        pass

    assert types.FunctionType(foo.__code__, globals(), "foo",
                              ("a", "b"), None)(1, 2) is None

def test_function_type_callable_4():
    def foo(a, b, c, d):
        pass

    assert types.FunctionType(foo.__code__, globals(), "foo",
                              ("a", "b", "c", "d"), None)(1, 2, 3, 4) is None

def test_function_type_callable_5():
   
