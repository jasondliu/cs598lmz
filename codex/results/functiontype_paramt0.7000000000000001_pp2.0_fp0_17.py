from types import FunctionType
list(FunctionType(c, globals(), 'c'))

# %%
# More complicated example

from types import FunctionType
from inspect import signature

def make_adder(number):
    def real_adder(number2):
        return number + number2
    return FunctionType(
        real_adder.__code__,
        {},
        real_adder.__name__,
        signature(real_adder),
        real_adder.__closure__,
    )


adder = make_adder(2)
adder(3)

# %%
# The builtin types allow to set attributes on classes themselves
# We can't do that, because this is not a class, but a function
# So, we need to hack around it

from types import FunctionType
from inspect import signature

def make_adder(number):
    def real_adder(number2):
        return number + number2
    adder = FunctionType(
        real_adder.__code__,
        {},
        real_adder.__name__,
        signature(real_adder),
        real_adder.__closure__,
