from types import FunctionType
a = (x for x in [1])
b = [1]
c = {1}
d = set()
e = 1
f = ''
g = dict()
h = FunctionType(lambda : 1, None, None, None, None)
i = type(lambda : 1)
j = {}
k = ()
l = type
m = type(1)
n = type(a)
o = type(k)
p = type(j)
q = type(type)

print(f'a = {a}, type is: {type(a)}')
print(f'b = {b}, type is: {type(b)}')
print(f'c = {c}, type is: {type(c)}')
print(f'd = {d}, type is: {type(d)}')
print(f'e = {e}, type is: {type(e)}')
print(f'f = {f}, type is: {type(f)}')
print(f'g = {g}, type is: {type(g)}')
print(f'h = {h}, type is: {type(h)}
