from types import FunctionType
a = (x for x in [1])
b = [1, 2, 3]

c = 10
def fun(x):
    return x * 2
print(isinstance(a, GeneratorType))
print(isinstance(b, list))
print(isinstance(c, int))
print(isinstance(fun, FunctionType))
print(isinstance(fun, FunctionType))


def add2num(n1, n2):
    pass

para =(1, 2)
add2num(*para)

a = {1: 2, 'c': 'd'}
print(a)
a['b'] = 2
print(a)
a.update({'c': 3})
print(a)
print(a.get('e', 'not found in dict'))
a.setdefault(7, 9)
print(a)

print(hash((1,2)))
print(hash({"name": "foo", "age": 20}))

a = 'a'
b = a
print(id(a))
print(id(b))

a = a + 'b'

