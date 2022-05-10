import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)
fun = FUNTYPE(lambda x,y: x+y)
fun(1,2)

#Argument Checking
def add_ints(x, y):
    """
    Add two ints
    """
    return x + y

add_ints.__annotations__

def add_ints(x:int, y:int) -> int:
    """
    Add two ints
    """
    return x + y
add_ints.__annotations__
add_ints(1, 2)
add_ints(1.0, 2.0)

def foo(x):
    if not isinstance(x, int):
        raise TypeError('x must be an integer')
    return x

#Functions as Arguments
def add_ints(x:int, y:int) -> int:
    """
    Add two ints
    """
    return x + y

add_ints(1.0, 2.0)
add_ints('a', 'b')
