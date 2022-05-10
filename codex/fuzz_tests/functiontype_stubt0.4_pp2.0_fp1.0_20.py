from types import FunctionType
a = (x for x in [1])
b = [1,2,3]
c = {1,2,3}
d = {1:2}
e = FunctionType(lambda x:x,globals())
f = type
g = int
h = str
i = bool
j = list
k = dict
l = set
m = tuple
n = object
o = type(None)
p = type(Ellipsis)
q = type(NotImplemented)
r = type(1j)
s = type(1)
t = type(1.0)
u = type(1.0+0j)
v = type(1L)
w = type(u"")
x = type(b"")
y = type(bytearray(b""))
z = type(range(0))

#print(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z)
print(a)
print(b)

