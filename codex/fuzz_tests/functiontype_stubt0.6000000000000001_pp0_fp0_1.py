from types import FunctionType
a = (x for x in [1])
b = [1, 2, 3]
type(a)

type(b)

isinstance(b, list)

isinstance(a, GeneratorType)

isinstance(b, Iterable)

isinstance(a, Iterable)

isinstance((x for x in range(10)), Iterator)

isinstance(iter([]), Iterator)

isinstance([], Iterable)

isinstance([], Iterator)

isinstance(iter([]), Iterable)

isinstance(int, type)

isinstance(int, object)

isinstance(object, type)

isinstance(object, object)

isinstance(object, FunctionType)

isinstance(len, FunctionType)

isinstance(iter, FunctionType)

isinstance(object, FunctionType)

isinstance(FunctionType, type)

isinstance(FunctionType, object)

isinstance(FunctionType, FunctionType)

isinstance(object, FunctionType)

isinstance(len, FunctionType)

isinstance(object, FunctionType)
