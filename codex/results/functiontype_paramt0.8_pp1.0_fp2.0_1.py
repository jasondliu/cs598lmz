from types import FunctionType
list(FunctionType(b1.__code__, globals={'a': a, 'b': b}).__closure__)

# You can only change the free variables if you have an __closure__
# and you always have an __closure__ if you have free variables

b2 = FunctionType(b.__code__, globals(), None, (a, b))
b2.__closure__  # doctest: +ELLIPSIS

# To make the __closure__ of an existing function available,
# set __closure__ to None:
b3 = FunctionType(b.__code__, globals(), None, None)
b3.__closure__  # doctest: +ELLIPSIS

# When you do this, the new __closure__ is initialized to the
# original __closure__:
b3.__closure__ = None
b3  # doctest: +ELLIPSIS

# The __closure__ attribute should obey the descriptor protocol:
def f():
    def f():
        return 1
    f.__closure__ = (2,)
    return f()

f()


# Check that an
