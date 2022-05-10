gi = (i for i in ())
# Test gi.gi_code.co_flags & 0x20

# Check nested generators

def f():
    def g():
        yield 0
        yield 1
        yield 2
    yield from g()
    yield 3

gf = f()
print(list(gf))

# Check nested generators

def f():
    def g():
        yield 0
        yield 1
        yield 2
    return g()

gf = f()
print(list(gf))

# Check nested generators

def f():
    def g():
        yield 0
        yield 1
        yield 2
    return g

gf = f()()
print(list(gf))

# Check nested generators

def f():
    def g():
        yield 0
        yield 1
        yield 2
    return g

gf = f()
print(list(gf()))

# Check nested generators

def f():
    def g():
        yield 0
        yield 1
        yield 2
    yield from g()
    yield 3

gf = f()
print(list(
