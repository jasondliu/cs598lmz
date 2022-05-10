from types import FunctionType
a = (x for x in [1])
print(type(a))
print(a)
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, Generator))
print(isinstance(a, FunctionType))

print(isinstance([], Iterator))
print(isinstance([], Iterable))
print(isinstance([], Generator))
print(isinstance([], FunctionType))

print(isinstance((x for x in [1]), Iterator))
print(isinstance((x for x in [1]), Iterable))
print(isinstance((x for x in [1]), Generator))
print(isinstance((x for x in [1]), FunctionType))

print(isinstance(iter([]), Iterator))
print(isinstance(iter([]), Iterable))
print(isinstance(iter([]), Generator))
print(isinstance(iter([]), FunctionType))

print(isinstance(iter((x for x in [1])), Iterator))
print(isinstance(iter((x for x in [1])), Iterable))
print(isinstance
