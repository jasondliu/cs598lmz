from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
c = {x for x in [1]}
d = {x: x for x in [1]}
e = FunctionType(lambda: None, globals())
f = lambda: None
g = type(None)
h = type(object)
i = type(type)
j = type(int)
k = type(iter)
l = type(FunctionType)
m = type(lambda: None)
n = type(type)
o = type(type(None))
p = type(object())

a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p

# EOF
