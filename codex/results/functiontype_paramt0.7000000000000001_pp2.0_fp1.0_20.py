from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__, closure=f.__closure__)
      for f in (fn, fn2))
# [<function __main__.fn>, <function __main__.fn2>]
# etc.

# fn2 is a closure.  It needs to access x from its environment.
def make_adder(x):
    def adder(y):
        return x + y
    return adder

adder1 = make_adder(1)
adder2 = make_adder(2)
adder1(2), adder2(2)
# (3, 4)

# Built-in functions (even if written in C) are still first-class objects:
callable(len)
# True

# And we can retrieve their source code:
print(len.__doc__)
# len(object) -> integer
#
# Return the number of items of a sequence or mapping.

# The directory built-in is handy for introspection:
dir(len
