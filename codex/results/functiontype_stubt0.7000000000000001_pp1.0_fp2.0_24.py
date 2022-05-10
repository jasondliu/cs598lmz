from types import FunctionType
a = (x for x in [1])
a.__class__

b = map(lambda x:x, [1])
b.__class__

c = [1]
c.__class__

d = 1
d.__class__

e = FunctionType(lambda x:x, globals())
e.__class__

f = lambda x:x
f.__class__

g = ''
g.__class__

h = {}
h.__class__

i = ()
i.__class__

j = set()
j.__class__

k = frozenset()
k.__class__

l = True
l.__class__

m = None
m.__class__

n = object()
n.__class__

o = object
o.__class__

p = memoryview(b'')
p.__class__

q = bytearray()
q.__class__

r = buffer(b'')
r.__class__

s = type
t = type(t)
s.__class__


