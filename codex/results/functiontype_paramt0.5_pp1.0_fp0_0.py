from types import FunctionType
list(FunctionType(lambda a, b, c: a + b + c, {}, None, None, None).__code__.co_varnames)

# function with closure
def f(x):
    def g(y):
        return x + y
    return g

g = f(1)

# inspect.getclosurevars(g)

# inspect.getclosurevars(g)
import inspect
inspect.getclosurevars(g)

# inspect.getclosurevars(g).nonlocals
inspect.getclosurevars(g).nonlocals

# inspect.getclosurevars(g).nonlocals['x']
inspect.getclosurevars(g).nonlocals['x']

# inspect.getclosurevars(g).nonlocals['x'].cell_contents
inspect.getclosurevars(g).nonlocals['x'].cell_contents

# inspect.getclosurevars(g).globals
inspect.getclosurevars(g).globals

# inspect.getclosurevars(g
