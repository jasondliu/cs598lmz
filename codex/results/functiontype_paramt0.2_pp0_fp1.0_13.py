from types import FunctionType
list(FunctionType(lambda x: x, globals()) for x in range(10))

# [<function <lambda> at 0x7f7b8c2e8c80>, <function <lambda> at 0x7f7b8c2e8d08>, <function <lambda> at 0x7f7b8c2e8d90>, <function <lambda> at 0x7f7b8c2e8e18>, <function <lambda> at 0x7f7b8c2e8ea0>, <function <lambda> at 0x7f7b8c2e8f28>, <function <lambda> at 0x7f7b8c2e8fb0>, <function <lambda> at 0x7f7b8c2e9038>, <function <lambda> at 0x7f7b8c2e90c0>, <function <lambda> at 0x7f7b8c2e9148>]

# The following is a more readable version of the above:

def make_function(i):
    return FunctionType(lambda x: x, globals())

