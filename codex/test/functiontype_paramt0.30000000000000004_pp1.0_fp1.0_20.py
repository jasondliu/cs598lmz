from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__, closure=f.__closure__)
     for f in (lambda x: x, lambda x=1: x))
# [<function <lambda> at 0x7f0c8e8f7f28>, <function <lambda> at 0x7f0c8e8f7ea0>]

# The same as above, but with a closure
def make_adder(n):
    def add(x):
        return x + n
    return add

add3 = make_adder(3)
add5 = make_adder(5)

list(FunctionType(add3.__code__, add3.__globals__, name=add3.__name__,
                  argdefs=add3.__defaults__, closure=add3.__closure__)
     for add3 in (add3, add5))
# [<function make_adder.<locals>.add at 0x7f0c8e8f7
