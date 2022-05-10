from types import FunctionType
a = (x for x in [1])
print(isinstance(a, FunctionType))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))
print(isinstance(a, Generator))

print(isinstance(a, (Iterator, Iterable, Generator)))

print(isinstance(a, (Iterator, Iterable, FunctionType)))

print(isinstance(a, (Iterator, Iterable, Generator, FunctionType)))

print(isinstance(a, (Iterator, Iterable, Generator, FunctionType, list)))

print(isinstance(a, (Iterator, Iterable, Generator, FunctionType, list, tuple)))

print(isinstance(a, (Iterator, Iterable, Generator, FunctionType, list, tuple, dict)))
