from types import FunctionType
a = (x for x in [1])
print(type(a))
def fun():
    yield 2
print(type(fun))
print(isinstance(fun,FunctionType))
print(isinstance(a,FunctionType))
print(dir(fun))
print(dir(a))
def fun():
    pass
print(type(fun))
print(isinstance(fun,FunctionType))

a = {x:x**2 for x in range(10) if x % 2 ==0}
print(a)

g = (x for x in range(10))
print(iter(g) is g)

g = (x for x in range(10))
for a in g:
    print(a)

g = (x for x in range(10))
for a in g:
    print(a)


# a = open('a.txt','w')
# print(a)
# a.close()

a = open('a.txt','w')
a.write('aaaaa\n')
a.write('bbb\n')
a.close()

a = open('a.
