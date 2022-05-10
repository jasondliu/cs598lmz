from types import FunctionType
list(FunctionType(function_2.__code__, globals(), 'my_func_3', function_2.__defaults__, function_2.__closure__))

def function_3(a, b, c, d):
    return a + b + c + d

function_3.__code__ = function_2.__code__
function_3(1, 2, 3, 4)

function_3.__code__ = function_1.__code__
function_3(1, 2, 3, 4)

try:
    function_3.__code__ = function_3.__code__
except TypeError as e:
    print(e)

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('Calling decorated function')
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def example():
    """Docstring"""
    print('Called example function')
example.__name__
example.__doc__

def example():
    """Docstring"""
    print('Called
