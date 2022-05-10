from types import FunctionType
list(FunctionType(lambda: None, globals()))

#
# 
#
# isinstance

#
# 
#
import types

a = 1
print a
print isinstance(a, int)
print isinstance(a, (int, bool, float))

class A(object):
    pass

class B(A):
    pass

a = A()
isinstance(a, A)
isinstance(a, B)
isinstance(a, (A, B))

#
# 
#
a = [1, 2, 3]
a[1:]
a[1:2]
a[:-1]
a[:]

#
# 
#
a = [1, 2, 3]
a[::-1]

#
# 
#
a = [1, 2, 3, 4]
a[-1]
a[0]
a[-1:0:-1]
a[-1:0:-2]

#
# 
#
# zip

#
# 
#
a = [1
