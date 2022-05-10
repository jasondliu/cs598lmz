from types import FunctionType
a = (x for x in [1])
type(a)
print(isinstance(a, Iterator))  #
print(isinstance(a, Iterable))  #
print(isinstance('abc', Iterator))  #
print(isinstance([1, 2, 3], Iterable))  #
print(isinstance(100, Iterator))  #
print(isinstance('abc', Iterable))  #
print(isinstance(iter, Iterable))  #
print(isinstance(iter, Iterator))  #
print(isinstance(iter('abc'), Iterable))  #
print(isinstance(iter('abc'), Iterator))  #
print(isinstance(abs, Iterator))  #
print(isinstance(abs, Iterable))  #
print(isinstance(FunctionType, Iterable))  #
print(isinstance(FunctionType, Iterator))  #

import collections

print(isinstance(iter(FunctionType), Iterable))  #
print(isinstance(iter(FunctionType), Iterator))  #
print(isinstance(iter(FunctionType), collections.Iterator))  #
print(is
