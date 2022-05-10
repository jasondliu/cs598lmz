from types import FunctionType
a = (x for x in [1])
print(type(a))

b = FunctionType(a.gi_code, a.gi_frame.f_globals)
print(b)
# <class 'generator'>
# <function <genexpr> at 0x10eb13378>
# <function <genexpr>.<locals>.<genexpr> at 0x10eb13620>

c = b()
print(c)
print(type(c))
# <generator object <genexpr>.<locals>.<genexpr> at 0x10eb13f50>
# <class 'generator'>

d = list(b())
print(d)
# [1]

print('--------------------------------')


def gen_fib(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


def fib(n):
    a, b = 0, 1
    l = []
    for i in range(n):
        l.append(a)
        a, b = b, a + b

