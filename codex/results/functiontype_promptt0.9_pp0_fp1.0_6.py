import types
# Test types.FunctionType


def f_type():
    try:
        type(f_type)
    except:
        print('Bug in type([])')


try:
    if type(f_type) != types.FunctionType:
        print('Bug in type([])')
except:
    print('Bug in type([])')
# Test types.LambdaType


def f_lambda(): return lambda x: x


class A(object):
    fib = f_lambda()


try:
    if type(A.fib) != types.LambdaType:
        print('Bug in type(A.fib)')
except:
    print('Bug in type(A.fib)')
# Test types.GeneratorType


def f_generator(n):
    while (n > 0):
        n -= 1
        yield n


g = f_generator(10)

try:
    if type(g) != types.GeneratorType:
        print('Bug in type(g)')
except:
    print('Bug in type(g)')
#
