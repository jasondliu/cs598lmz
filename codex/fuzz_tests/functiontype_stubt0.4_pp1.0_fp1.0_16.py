from types import FunctionType
a = (x for x in [1])
print(a)
print(type(a))
print(type(a) == GeneratorType)
print(type(a) == FunctionType)

print(type(print))
print(type(print) == FunctionType)

print(type(lambda x: x) == FunctionType)

print(type(x for x in range(10)) == FunctionType)

print(type(abs) == FunctionType)

print(type(a) == FunctionType)

print(type(a) == GeneratorType)

print(type(a) == IteratorType)

print(type(a) == IterableType)

print(type(a) == ListType)

print(type(a) == TupleType)

print(type(a) == DictType)

print(type(a) == SetType)

print(type(a) == StringType)

print(type(a) == UnicodeType)

print(type(a) == IntType)

print(type(a) == LongType)

print(type(a) ==
