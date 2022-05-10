from types import FunctionType
a = (x for x in [1])
a.__next__()

# isinstance(a, FunctionType)
# isinstance(a, types.GeneratorType)

def fib(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

fib(100)

for i in fib(100):
    print(i)

# yield from

def g1(gen):
    yield from gen

def main():
    g = g1()
    g.send(None)

# 递归调用

def g2(gen):
    yield from gen

def main():
    g = g2(g1(g2(g1(g2(...)))))
    g.send(None)

# 并发执行

def g2(gen):
    yield from gen

def main():
    g1 = g2(...)
    g2 = g2(...)
    g1.send(None)
    g2.send(None
