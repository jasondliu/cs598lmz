from types import FunctionType
a = (x for x in [1])
print(type(a))
print(a.__next__())
print(a.__next__())

b = iter([1,2,3])
print(type(b))
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())

c = (i for i in range(1,10) if i % 2 == 0)
print(type(c))
for i in c:
    print(i)

c = [i for i in range(1,10) if i % 2 == 0]
print(type(c))
for i in c:
    print(i)

print(type(range))
print(type(FunctionType))
print(type(sum))
print(type(abs))

print("--------------------------------")

d = filter(lambda x: x % 2 == 0, range(1,10))
print(type(d))
# print(d.__next__())
# print(d.__next__())
# print(d.__next__
