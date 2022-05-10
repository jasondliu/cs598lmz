from types import FunctionType
list(FunctionType(lambda x: x+1, {}, None, None, None))
 
# (1, 2, 3)
def f(x): return x+1
list(FunctionType(f.__code__, f.__globals__, f.__name__, f.__defaults__, f.__closure__))
 
# (1, 2, 3)
list(f)

# (1, 2, 3)
 
# (1, 2, 3)
