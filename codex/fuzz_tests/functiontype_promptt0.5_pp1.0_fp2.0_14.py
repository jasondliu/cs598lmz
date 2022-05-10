import types
# Test types.FunctionType
def foo():
    pass

def bar(a, b, c):
    pass

def baz(a, b, c, *args, **kwargs):
    pass

def gen():
    yield 1

def gen2(a):
    yield a

def gen3(a, b):
    yield a
    yield b

def gen4(a, b):
    yield a
    yield b
    yield c

def gen5(a, b):
    yield a
    return b

def gen6(a, b):
    yield a
    return b
    yield c

def gen7(a, b):
    yield a
    return
    yield b

def gen8(a, b):
    yield a
    return

def gen9(a, b):
    yield a
    return b
    return c

def gen10(a, b):
    yield a
    return b

def gen11(a, b):
    yield a
    return b
    return

def gen12(a, b):
   
