from types import FunctionType
list(FunctionType(f.func_code, f.func_globals, 'new', f.func_defaults, f.func_closure).func_closure)

def f():
    a = 1
    b = 2
    return a + b

f.__closure__

f.__closure__[0].cell_contents

def adder(a, b):
    def add(x, y):
        return x + y
    return add(a, b)

adder(1, 2)

def adder(a, b):
    def add(x, y):
        return x + y
    return add

adder(1, 2)
