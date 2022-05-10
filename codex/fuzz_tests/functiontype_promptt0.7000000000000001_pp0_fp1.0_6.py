import types
# Test types.FunctionType, types.LambdaType

# function type is callable
def test_function_type():
    def f():
        pass
    assert type(f) == types.FunctionType
    f()


# lambda is callable
def test_lambda_type():
    f = lambda : True
    assert type(f) == types.LambdaType
    f()


# general callable (function and lambda)
def test_general_callable():
    f = lambda : True
    assert callable(f)
    def f():
        pass
    assert callable(f)

# builtin functions are callable
def test_builtin_callable():
    # len is a built-in function
    assert callable(len)


# builtin methods are callable
def test_builtin_method_callable():
    # upper is a built-in method of string type
    assert callable("".upper)


# user defined methods are callable
def test_user_defined_method_callable():
    class A(object):
        def f(self):

