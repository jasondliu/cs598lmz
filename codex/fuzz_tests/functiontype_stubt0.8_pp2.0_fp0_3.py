from types import FunctionType
a = (x for x in [1])
type(a)

a1 = iter([1])
type(a1)

a = (x for x in [1])
type(a)
a1 = (x for x in [1])
type(a1)

a = (x for x in [1])
a1 = (x for x in [1])
type(a) == type(a1)

a = (x for x in [1])
a1 = (x for x in [1])
a == a1

a = (x for x in [1])
a1 = (x for x in [1])
hash(a) == hash(a1)

a = (x for x in [1])
b = (x for x in [1])
hash(a) == hash(b)

a = (x for x in [1])
b = (x for x in [2])
hash(a) == hash(b)


a = (x for x in [1])
type(a) == FunctionType

a = (x for x in [1])
isinstance
