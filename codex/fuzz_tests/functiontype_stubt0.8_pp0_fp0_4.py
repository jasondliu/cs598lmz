from types import FunctionType
a = (x for x in [1])

isinstance(a, FunctionType)

def f():
    return "f"

isinstance(f, FunctionType)
