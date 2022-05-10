from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
c = {x for x in [1]}
d = {x: x for x in [1]}
e = FunctionType(lambda x: x, globals())
f = lambda x: x
g = type(lambda x: x)
h = type(type(lambda x: x))
i = type(FunctionType(lambda x: x, globals()))
j = type(type(FunctionType(lambda x: x, globals())))
k = type(type(type(FunctionType(lambda x: x, globals()))))
l = type(type(type(type(FunctionType(lambda x: x, globals())))))
m = type(type(type(type(type(FunctionType(lambda x: x, globals()))))))
n = type(type(type(type(type(type(FunctionType(lambda x: x, globals())))))))
o = type(type(type(type(type(type(type(FunctionType(lambda x: x, globals()))))))))
p = type(type(type(type(type
