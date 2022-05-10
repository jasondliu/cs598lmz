from types import FunctionType
a = (x for x in [1])

print(isinstance(a, GeneratorType))
print(isinstance(abs, FunctionType))
print(isinstance(a, Iterator))
print(isinstance((x for x in range(10)), Iterable))

print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))

print('==========================================================================')
print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))
print(isinstance(iter([]), Iterable))

print('==========================================================================')
print(isinstance([], GeneratorType))
print(isinstance(iter([]), GeneratorType))

print('==========================================================================')
# iter list:
print('for x in [1, 2, 3, 4, 5]:')
for x in [1, 2, 3, 4, 5]:
