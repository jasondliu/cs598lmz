from types import FunctionType
a = (x for x in [1])
a = (x for x in [1, 2])  # Noncompliant {{This generator expression contains 2 items, which exceeds the threshold of 1.}}
#    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
b = tuple(x for x in [1])

def foo():
    return a[0] + 1

def some_generator():
    yield 0
    return

def gen():
    with open("test.txt") as f:
        line = f.readline()
        while line:
            line = f.readline()
            yield line

def gen_with_try():
    try:
        with open("test.txt") as f:
            lines = f.readlines()
            while lines:
                lines = f.readlines()
                yield lines
    except:
        yield []

c = (x for x in range(100))


def fun():
    return c[0]  # belongs to c

for c in range(10):
    print(c)
    pass


def funct
