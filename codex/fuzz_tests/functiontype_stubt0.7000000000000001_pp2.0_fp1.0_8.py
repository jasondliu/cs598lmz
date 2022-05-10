from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
b = (x for x in [1])
print(b)
print(type(b))

'''
a = (x for x in [1])
print(a)
print(type(a))
b = (x for x in [1])
print(b)
print(type(b))
'''
'''
a = (x for x in [1])
print(a)
print(type(a))
print(a.__next__())
print(a.__next__())

print(a.__next__())
'''
'''
a = (x for x in [1, 2, 3])
print(a)
print(type(a))
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(next(a))
'''
'''
a = (x for x in [1, 2, 3])
print(a)
print(type(a))
for i in a:
    print(i)

