from types import FunctionType
list(FunctionType(f.__code__, f.__globals__).__closure__)

#[<cell at 0x0000029FCB3F2728: int object at 0x0000029FCB3D0C70>,
# <cell at 0x0000029FCB3F27A8: int object at 0x0000029FCB3D0C50>]

# The two cells correspond to the two variables used in the nested scope of f.
# The values of the cells are the original value of n and n squared in the outer scope.

# You can also get a function's free variables (that is, the values of variables from
# the enclosing scope) with the __closure__ attribute.

a = 10
b = 11

def f(x):
    # The closure contains the variable from the enclosing scope
    return lambda y: x + y + a + b

c = f(1)
c(2) # 25
c.__closure__[0].cell_contents # 1

# Notice that the __closure__ attribute contains a tuple of cells, each one
# corresponding to a variable in
