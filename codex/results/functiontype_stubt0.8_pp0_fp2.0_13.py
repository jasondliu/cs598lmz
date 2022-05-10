from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, FunctionType))
print(a)
for n in a:
    print(n)

#逆序，列表本身反向
l = ['dog', 'cat', 'monkey']
print(l[::-1])
print(list(reversed(l)))


l = ['a', 'b', 'c', 'd', 'f']
print(id(l))
l.reverse()
print(l)
print(id(l))

#排序
l = ['a', 'c', 'b', 'F', 'D']
l.sort(key=str.lower, reverse=True)
print(l)

l = sorted([-1, 2, 1, -2], key=abs, reverse=True)
print(l)

#列表反向
l = ['a', 'b', 'c', 'd', 'f']
print(l[::-1])
print(l)

#map
