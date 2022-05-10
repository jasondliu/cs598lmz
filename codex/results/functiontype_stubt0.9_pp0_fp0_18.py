from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
isinstance(a, GeneratorType)

a2 = [x for x in [1]]
b2 = [x for x in [1]]
isinstance(a2, list)

myabs = FunctionType(abs.__code__, abs.__globals__, 'myabs', None, None)
myabs(1)

type(int('123'))



def myadd(a, b):
    if not isinstance(a, int):
        raise TypeError('bad operand type')
    return a + b
    
    
def mysum(*args):
    if not isinstance(args[0], int):
        raise TypeError('bad operand type')
    sum = 0
    for arg in args:
        sum += arg
    return sum

# myabs('123')
# mysum(1, 2, 3, 'a')


def mylog(func):
    def wrapper(*args, **kw):
        print('%s() called' % func.__name__)
        return func(*
