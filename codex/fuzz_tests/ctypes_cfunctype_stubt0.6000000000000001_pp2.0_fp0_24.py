import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello!"

# fun()
# 'Hello!'
fun.__name__
# 'fun'

# fun.__name__ = "new_fun"
# fun.__name__
# 'new_fun'

# fun()
# 'Hello!'

#The function object still has a reference to the original name, but this is not used by the interpreter.

#The Python interpreter will use the name of the function object to display the function in tracebacks, and to display the function in the help() function.

#2.2.2
#The code attribute
#The code attribute is a read-only attribute that returns a tuple with information about how the function was created.

def fun():
    return "Hello!"

fun.__code__
# <code object fun at 0x7f3c3b3d5030, file "<stdin>", line 1>

#The code object returned by the code attribute has the following attributes:

#co_argcount: The number of arguments the function takes, excluding the argument with the * and ** syntax.
#co_consts: A
