from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__, closure=f.__closure__)
     for f in (lambda: (yield from range(10)),
               lambda x=5: (yield from range(x)),
               lambda x, y=5: (yield from range(x + y))))

# [<function <lambda> at 0x7f2c5d7e5d08>,
#  <function <lambda> at 0x7f2c5d7e5e18>,
#  <function <lambda> at 0x7f2c5d7e5ea0>]

# The function is not a generator function, but a normal function that returns a generator.
# The generator is created when the function is called.

# The function is not a generator function, but a normal function that returns a generator.
# The generator is created when the function is called.

# The function is not a generator function, but a normal function that returns a generator.
# The generator is created when the
