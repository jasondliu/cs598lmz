from types import FunctionType
list(FunctionType(repr.__code__)(1, 2, 3))

# the first arg of FunctionType is the code object
# the other args are positional args
FunctionType(repr.__code__, {}, 'closure')
# the last arg is the closure of the function

import types
def test_closure():
    x = 1
    y = 2
    return types.FunctionType(repr.__code__, {}, 'closure')

test_closure()()

# the closure is a tuple of cells
test_closure().__closure__

import dis
dis.dis(test_closure)

# the code object is an object which have attributes
# co_code:       the machine code
# co_consts:     the constant used in the code
# co_varnames:   the local variable names
# co_names:      the global variable names
# co_argcount:   the count of positional args
# co_kwonlyargcount: the count of keyword args
# co_nlocals:    the count of local var count
# co_stacksize:  the stack depth
#
