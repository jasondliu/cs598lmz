from types import FunctionType
list(FunctionType(j,globals(),'j').__code__.co_consts)

set.__doc__

def n(): return 'something'
print(n)

n.__doc__ = 'lool'
print(n.__doc__)
print(n())


# from func_tools import trace

# @trace
def square(x): return x * x
#print(square.__code__.co_consts)
# print(square(4))
# print(square(square(4)))

# square.__code__.co_consts
# square.__dict__
# square(4)
# square.__code__ = 42
# square(4)

# @trace
# def g(x):
#     y = square(x)
#     return y - x
# print(g(2))

#g.__code__.co_consts



# def square(x):
#    return x * x

# square(5)

# square.__code__.co_consts

# square.__code
