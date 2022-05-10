from types import FunctionType
a = (x for x in [1])
isinstance(a, GeneratorType)

b = [1, 2]
isinstance(b, Iterable)

c = (x for x in [1])
isinstance(c, Iterator)

d = {'a': 1}
isinstance(d, Mapping)

e = [1, 2, 3]
isinstance(e, MutableSequence)

f = (1, 2, 3)
isinstance(f, MutableSet)

g = {'a': 1, 'b': 2}
isinstance(g, MutableMapping)

h = [1, 2, 3]
isinstance(h, Sequence)

i = (1, 2, 3)
isinstance(i, Set)

j = {'a': 1, 'b': 2}
isinstance(j, MappingView)

k = [1, 2, 3]
isinstance(k, Sized)

l = (1, 2, 3)
isinstance(l, Sized)

m = {'a': 1, 'b': 2}

