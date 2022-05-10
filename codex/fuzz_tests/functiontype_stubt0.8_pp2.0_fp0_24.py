from types import FunctionType
a = (x for x in [1])
b = (x for x in [2])
c = (x for x in [3])
d = a.next()
e = b.next()
f = c.next()
h = (d, e, f)
print(h)

def test(x, y):
    return x + y
t = (10, 20)
t = test(*t)
print(t)
