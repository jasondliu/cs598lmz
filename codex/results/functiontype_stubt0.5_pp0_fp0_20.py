from types import FunctionType
a = (x for x in [1])
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, Iterator))

for i in a:
    print(i)

b = [1, 2, 3]

c = (x for x in b)

for i in c:
    print(i)

d = (x for x in b)

for i in d:
    print(i)

e = (x for x in b)

for i in e:
    print(i)

f = (x for x in b)

for i in f:
    print(i)

g = (x for x in b)

for i in g:
    print(i)

h = (x for x in b)

for i in h:
    print(i)

i = (x for x in b)

for i in i:
    print(i)

j = (x for x in b)

for i in j:
    print(i)

k = (x
