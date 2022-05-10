from types import FunctionType
list(FunctionType(f, globals(), 'f') for f in [lambda a, b: a + b, lambda a, b: a * b])

# 参数检查
def f(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

f(1, 2)
f(1, 2, c=3)
f(1, 2, 3, 'a', 'b')
f(1, 2, 3, 'a', 'b', x=99)
args = (1, 2, 3, 4)
kw = {'x': 99}
f(*args, **kw)

# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1, 2))
print(calc())

nums = [1, 2, 3]
print(cal
