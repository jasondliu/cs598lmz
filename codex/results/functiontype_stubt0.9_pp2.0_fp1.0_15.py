from types import FunctionType
a = (x for x in [1])
b = (x for x in [1, 2])
print(type(a))
print(type(b))

print(a.__next__())
print(type(a))
print(a.__next__())
print(type(a))
print(next(b))

def fact(n):
    '''
    返回从1到n的阶乘
    '''
    if not isinstance(n, (int, float)):
        raise TypeError("Error params")
    if n < 1:
        raise ValueError("arg must be larger than zero")
    if n == 1:
        return 1
    return n * fact(n - 1)
print(fact(10))
print(fact(10.0))
# print(fact("aaa"))
print(fact(1))
# print(fact(-10))

def factr(n):
    '''
    返回从1到n的阶乘
    '''
    if not isinstance(n, (int, float)
