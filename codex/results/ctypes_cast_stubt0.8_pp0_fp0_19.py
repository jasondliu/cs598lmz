import ctypes
ctypes.cast(0, ctypes.py_object).value

# Generator expressions
#(sum(row) for row in M)

# Tuple assignment
t =  divmod(20, 8)
x, y = t

# Tuple unpacking
g = (sum(row) for row in M)
next(g)

# Sequence unpacking
seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in seq:
    print('a={0}, b={1}, c={2}'.format(a,b,c))

values = 1, 2, 3, 4, 5
a, b, *rest = values
print(a, b, rest)

# Named tuples
from collections import namedtuple
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
tokyo.population
tokyo.coordinates
tokyo[1]

# Slic
