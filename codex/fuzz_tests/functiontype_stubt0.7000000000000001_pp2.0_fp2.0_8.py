from types import FunctionType
a = (x for x in [1])
print(a)
b = (i for i in range(5))
print(b)
print(list(b))

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(6)
print(f)
print(next(f))
for x in f:
    print(x)

# 杨辉三角
def triangles():
    l = [1]
    while True:
        yield l
        l = [1] + [l[i] + l[i+1] for i in range(len(l)-1)] + [1]

#print(isinstance(triangles(), FunctionType))
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

def triangles_yield_from():
    l = [1]
    while True:
       
