import types
# Test types.FunctionType with a function with a closure.
def f(x):
    def g():
        return x
    return g

x = 1
g = f(x)
assert g.func_closure
assert len(g.func_closure) == 1
assert g.func_closure[0].cell_contents == 1

# Test types.FunctionType with a function with a closure that is a cell.
def f(x):
    def g():
        return x
    x = 2
    return g

x = 1
g = f(x)
assert g.func_closure
assert len(g.func_closure) == 1
assert g.func_closure[0].cell_contents == 2

# Test types.FunctionType with a function with a closure that is a cell and a freevar.
def f(x):
    def g():
        return y
    x = 2
    return g

x = 1
y = 3
g = f(x)
assert g.func_closure
assert len(g.func_closure) == 2
assert g.func_closure[0].
