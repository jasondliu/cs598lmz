from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name='my_func_gen',
                  argdefs=f.__defaults__,
                  closure=f.__closure__))

# second argument, f.__globals__, can be omitted in Python 3.7+
</code>

