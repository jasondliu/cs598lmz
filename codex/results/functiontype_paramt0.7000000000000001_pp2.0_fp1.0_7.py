from types import FunctionType
list(FunctionType(add.func_code, globals(), "add", add.func_defaults, add.func_closure).func_closure)

def make_adder(n):
    return lambda x: x + n
add5 = make_adder(5)
add5(10)

def make_adder_nonlocal(n):
    def adder(x):
        nonlocal n
        n += x
        return n
    return adder
add5_nonlocal = make_adder_nonlocal(5)
add5_nonlocal(10)
add5_nonlocal(10)
