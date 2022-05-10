from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(a.__iter__))
print(type(a.__iter__()) == a)
print(type(a.__next__))
print(type(a.__next__()) == int)
print(type(a.__next__))
print(type(a.__next__()) == int)
print(type(a.__next__))
print(type(a.__next__()) == StopIteration)
print(type(a.__next__))
print(type(a.__next__()) == StopIteration)
print(type(a.__next__))

try:
    print(type(a.__next__()) == StopIteration)
except StopIteration:
    print("StopIteration")

print(type(a.__next__))

try:
    print(type(a.__next__()) == StopIteration)
except StopIteration:
    print("StopIteration")

print(type(a.__next__))

try:
    print(type(a.__next
