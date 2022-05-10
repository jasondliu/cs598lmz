fn = lambda: None
gi = (i for i in ())
fn.__code__ = fn.__call__.__code__
print(sys.implementation.name)


def my_add(a, b):
    return a + b


def my_sub(a, b):
    return a - b


def my_mul(a, b):
    return a * b


def my_div(a, b):
    return a / b


A = my_add(user, sys)
print(A)
B = my_sub(user, sys)
print(B)
C = my_mul(user, sys)
print(C)
D = my_div(user, sys)
print(D)
