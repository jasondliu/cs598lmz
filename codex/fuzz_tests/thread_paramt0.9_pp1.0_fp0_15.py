import sys, threading
threading.Thread(target=lambda: sys.stdout.write("1\n")).start()
print("2")

# 3.
def f(i):
    return int(input())

x = [f(i) for i in range(3)]
print(x)

# 4.
def f(i):
    for j in range(4):
        yield j, i

x = [f(i) for i in range(3)]
print(x[0])
print(next(x[0]))
print(next(x[0]))
print(x[1])
print(list(x[0]))

# 5.
def f():
    return None, 1

a, (b, c) = f()
print(a, b, c)

# 6.
def f(a, b=0, *c, **kw):
    print(a, b, c, kw)

f(1, *(2, 3), **{'x': 4, 'y': 5})

# 7.
d = dict(zip(('a', 'b
