from types import FunctionType
list(FunctionType(lambda x: x * x, globals(), 'square') for x in range(10))

# generators
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(10)
for x in f:
    print(x)

# yield from
def g1(gen):
    yield from gen

def main():
    g = g1()
    g.send(None)

# yield from
def g1(gen):
    yield from gen

def main():
    g = g1()
    g.send(None)

# yield from
def g1(gen):
    yield from gen

def main():
    g = g1()
    g.send(None)

# yield from
def g1(gen):
    yield from gen

def main():
    g = g1()
    g.send(None)

# yield from
def g1
