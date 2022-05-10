from types import FunctionType
a = (x for x in [1])
print(a)
for x in a:
    print(x)
b = [1, 2, 3]
list(map(lambda x: x * x, b))

print(type(a))
print(type(b))
print(type(c))


def fun_add(x, y, f):
    return f(x) + f(y)

print(fun_add(-5, 6, abs))

def f(x):
    return x * x
print(f)
print(f(5))
print(f)
print(type(f))
print(type(abs))
print(f is abs)
print(type(f) == FunctionType)

ll = list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(ll)

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

print("*" * 50)

def add(x, y, f):
    return f(x
