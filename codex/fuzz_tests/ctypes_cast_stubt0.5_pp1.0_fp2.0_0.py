import ctypes
ctypes.cast(1, ctypes.py_object).value

# 3.
import sys
sys.getrefcount(1)

# 4.
a = [1, 2, 3]
b = a
a.append(4)
b

# 5.
def append_element(some_list, element):
    some_list.append(element)

data = [1, 2, 3]
append_element(data, 4)
data

# 6.
a = 5
type(a)
a = 'foo'
type(a)
'5'
type('5')

# 7.
a = 4.5
b = 2
# String formatting, to be visited later
print('a is {0}, b is {1}'.format(type(a), type(b)))
a / b
a = 5
isinstance(a, int)
a = 5; b = 4.5
isinstance(a, (int, float))
isinstance(b, (int, float))

# 8.
a = 'foo'
getattr(a, 'split')

