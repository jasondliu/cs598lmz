from types import FunctionType
a = (x for x in [1])
print(type(a))

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad operand type")
    if x >= 0:
        return x
    else:
        r
