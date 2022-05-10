from types import FunctionType
list(FunctionType(lambda a, b: a + b, globals(), "")(1, 2))

# https://bugs.python.org/issue35757
def f(x):
    if x % 2 == 0:
        return x // 2
    else:
        return x * 3 + 1

list(f(x) for x in range(1, 20))

# https://bugs.python.org/issue35757
def f(x):
    if x % 2 == 0:
        return x // 2
    else:
        return x * 3 + 1

list(f(x) for x in range(1, 20))

# https://bugs.python.org/issue35757
def f(x):
    if x % 2 == 0:
        return x // 2
    else:
        return x * 3 + 1

list(f(x) for x in range(1, 20))

# https://bugs.python.org/issue35757
def f(x):
    if x % 2 == 0:
        return x // 2
    else:
        return x *
