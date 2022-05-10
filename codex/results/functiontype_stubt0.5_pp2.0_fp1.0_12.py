from types import FunctionType
a = (x for x in [1])
a.__next__()

a = (x for x in [1,2,3])
next(a)
next(a)
next(a)
# next(a)

a = (x for x in [1,2,3])
for i in a:
    print(i)

a = (x for x in [1,2,3])
b = (x for x in [1,2,3])
print(a==b)
print(a is b)

a = (x for x in [1,2,3])
b = (x for x in [1,2,3])
print(next(a))
print(next(b))
print(next(a))
print(next(b))
print(next(a))
print(next(b))

a = (x for x in [1,2,3])
b = (x for x in [1,2,3])
print(a.__next__())
print(b.__next__())
print(a.__next__())
print(b.__next
