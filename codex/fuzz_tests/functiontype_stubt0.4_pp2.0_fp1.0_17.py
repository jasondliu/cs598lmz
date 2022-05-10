from types import FunctionType
a = (x for x in [1])
b = [1]
c = {1}
d = {1: 1}
e = [1, 2, 3]
f = {1, 2, 3}
g = {1: 1, 2: 2, 3: 3}
h = 1
i = 1.1
j = 'a'
k = True
l = None
m = FunctionType(lambda: None, {})
n = type
o = type(None)
p = type(lambda: None)
q = type(type(None))
r = type(type)
s = type(type(type(None)))
t = type(type(type))
u = type(type(type(type(None))))
v = type(type(type(type)))
w = type(type(type(type(type(None)))))
x = type(type(type(type(type))))
y = type(type(type(type(type(type(None))))))
z = type(type(type(type(type(type)))))

print(type(a))
print(type(b))
print(type(
