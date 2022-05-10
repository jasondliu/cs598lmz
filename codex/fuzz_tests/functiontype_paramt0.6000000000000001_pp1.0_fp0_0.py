from types import FunctionType
list(FunctionType(__code__, __globals__, 'foo',
                  __defaults__, __closure__) for __code__, (__globals__, __defaults__, __closure__) in __func_defaults__.items())

# examples/closures.py
def make_adder(n):
    def adder(x):
        return x + n
    return adder

add3 = make_adder(3)
add3(4)
make_adder(1000)(2)

# examples/closures2.py
def make_adder(n):
    x = [n]
    def adder(y):
        x[0] += y
        return x[0]
    return adder

add3 = make_adder(3)
add3(4)
add3(5)

# examples/closures3.py
def make_adder(n):
    def adder(x):
        nonlocal n
        n += x
        return n
    return adder

add3 = make_adder(3)
add3(4)
