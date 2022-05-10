import ctypes
ctypes.cast(_p, ctypes.py_object).value

# this is the first way of unpacking a list
(a,b, *_) = [1,2,3,4]
a, b

# this is the second way of unpacking a list
first, second, *remainder = [1,2,3,4]
first, second, remainder

# unpacking namedtuple
from collections import namedtuple
t = namedtuple('Student', ['rollno', 'name', 'marks'])
t.__new__(t, 1, 'A', 100)

(rollno, name, marks) = t(1, 'A', 100)
rollno, name, marks

# unpacking with generator expression
evens = (x for x in range(100) if x%2 == 0)
evens

a,b  = evens
a,b


## unpacking with function arguments
def fn(*args):
    return args
fn(1,2,3)

## unpacking with dictionary
d = {'a':1, 'b':2, '
