from types import FunctionType
a = (x for x in [1])
print(type(a))
print(isinstance(a, GeneratorType))
print(isinstance(a, FunctionType))
print(isinstance(a, Iterator))
print(isinstance(a, Iterable))

print(isinstance(a, (Iterator, Iterable)))

print(isinstance(a, (Iterator, Iterable, GeneratorType)))

print(isinstance(a, (Iterator, Iterable, FunctionType)))

print(isinstance(a, (Iterator, Iterable, FunctionType, GeneratorType)))

print(isinstance(a, (Iterator, Iterable, FunctionType, GeneratorType, object)))

print(isinstance(a, (Iterator, Iterable, FunctionType, GeneratorType, object, type)))

print(isinstance(a, (Iterator, Iterable, FunctionType, GeneratorType, object, type, int)))

print(isinstance(a, (Iterator, Iterable, FunctionType, GeneratorType, object, type, int, str)))

print(isinstance(a, (Iterator, Iterable, FunctionType, GeneratorType, object, type, int, str
