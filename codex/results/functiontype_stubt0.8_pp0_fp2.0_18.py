from types import FunctionType
a = (x for x in [1]).next
b = (x for x in [2]).next
assert type(a) == FunctionType
assert type(b) == FunctionType
assert a != b
assert hash(a) != hash(b)

# Generator with yield inside try/finally block
def gen1():
    try:
        yield -1
    finally:
        yield 0

assert list(gen1()) == [-1, 0]

def gen1a():
    try:
        yield -1
        try:
            yield -2
        finally:
            yield -3
    finally:
        yield 0

assert list(gen1a()) == [-1, -2, -3, 0]

def gen1b():
    try:
        yield -1
        try:
            yield -2
            raise Exception
        finally:
            yield -3
    finally:
        yield 0

try:
    g = gen1b()
    assert g.next() == -1
    assert g.next() == -2
    assert g.next() == -3
    g.next()
except Stop
