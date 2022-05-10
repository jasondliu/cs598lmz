from types import FunctionType
a = (x for x in [1])
print(isinstance(a, FunctionType))
b = {a:2}
assert isinstance(b, set) is False

import types
isinstance(b, types.DictType)
# isinstance of old-style class

T = tuple([1,2,3])
L = [4,5,6]
S = "Hello"
for i in T:
    print i


# res = 0
# for i in S:
#     print(i)
#     # print(ord(i))
#     res += ord(i)
# print(res)
print(eval('8/7'))
import string

print(string.ascii_lowercase)
print(string.octdigits)
print(string.digits)

import datetime
print(datetime.date.today())

def factorial(n):
    if n > 1:
        return reduce(lambda x, y: x * y, range(1, n + 1))
    elif n == 1:
        return 1
    else:
        return None


