import types
types.FunctionType.f_locals

def outer(x, y = 6):
    def inner():
        return x
    return inner

res = outer(100, 69)
res.__closure__
