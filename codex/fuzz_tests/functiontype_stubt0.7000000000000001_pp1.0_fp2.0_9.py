from types import FunctionType
a = (x for x in [1])
b = FunctionType
c = b()
d = 1
e = []
f = "2"
g = {1,2}
h = {}
i = None
j = b"7"
k = True
l = False
m = 0
n = object()

for obj in a,b,c,d,e,f,g,h,i,j,k,l,m,n:
    print(obj, type(obj), isinstance(obj, type))

print("---------------------------------------------------------")

for obj in a,b,c,d,e,f,g,h,i,j,k,l,m,n:
    print(type(obj), isinstance(type(obj), type))
    print(obj, isinstance(obj, type(obj)))
    print(type(obj), isinstance(obj, type(obj)))
    print("----------------")
