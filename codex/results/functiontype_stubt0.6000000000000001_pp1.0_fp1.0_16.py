from types import FunctionType
a = (x for x in [1])
b = [1,2,3]
c = '123'
d = {1:1,2:2}
e = {1,2,3}
f = FunctionType(lambda x:x,globals())
g = None
h = type
i = 1
j = 1.1
k = b'123'
l = True
m = bytearray(b'123')
n = memoryview(b'123')
o = range(3)
p = slice(1,2)
q = {1,2,3}
r = frozenset({1,2})
s = object()
t = type

t1 = (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t)

for x in t1:
    print(type(x))
