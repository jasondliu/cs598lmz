from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
c = {x for x in [1]}
d = {'1':1}
e = {'1'}
f = [x for x in [1]]

# print(isinstance(a, Iterator))
# print(isinstance(a, Iterable))
# print(isinstance(b, Iterator))
# print(isinstance(b, Iterable))
# print(isinstance(c, Iterator))
# print(isinstance(c, Iterable))
# print(isinstance(d, Iterator))
# print(isinstance(d, Iterable))
# print(isinstance(e, Iterator))
# print(isinstance(e, Iterable))
# print(isinstance(f, Iterator))
# print(isinstance(f, Iterable))

# iterator 一次性访问，只能往后访问
# iterable 可迭代对象，可以迭代多
