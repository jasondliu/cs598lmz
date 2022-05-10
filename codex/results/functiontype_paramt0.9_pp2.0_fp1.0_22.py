from types import FunctionType
list(FunctionType("", globals(), "").__code__.co_varnames)


def f(x):
    """
    Hello

    :param x: xx
    :return: bb
    """
    global b
    c = 1
    b = x * 2
    return x * 2

# from inspect import getsourcefile
# from os.path import realpath
# getsourcefile(f)  # realpath(f.__code__.co_filename)

# f(2)

# Print Global
print(globals())
print(globals().keys())

# Print Local
import sys
print(sys._getframe().f_locals)

print(globals()["b"])
print(globals()["c"])

a = [f, f(2)]
print(a)

# Get Var Names
print(dir(f))
print(dir(f.__code__))
print(f.__code__.co_varnames)
print(f.__code__.co_names)

d = ((2
