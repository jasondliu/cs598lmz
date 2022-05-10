from types import FunctionType
a = (x for x in [1])
b = [x for x in [1]]
c = {x for x in [1]}
d = {x:x for x in [1]}
e = 'x'
f = b'x'
g = 1
h = 1.0
i = 1j
j = lambda x: x
k = FunctionType(lambda x: x, {})

for x in [a, b, c, d, e, f, g, h, i, j, k]:
    print(type(x))

# <class 'generator'>
# <class 'list'>
# <class 'set'>
# <class 'dict'>
# <class 'str'>
# <class 'bytes'>
# <class 'int'>
# <class 'float'>
# <class 'complex'>
# <class 'function'>
# <class 'function'>
