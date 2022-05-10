from types import FunctionType
list(FunctionType(f.__code__).__globals__.items())

# 18.4.3
f.__globals__['math'].pi

# 18.4.4
import sys
globals() is sys.modules[__name__].__dict__

# 18.4.5
def test(a):
    a.append(1)
    print(a)
    a = [2, 3]
    print(a)

l = [1, 1]
test(l)
print(l)

a = [2, 3]
a.append(1)
print(a)
a = [2, 3]
print(a)

# 18.4.6
def test2(a):
    print(a)
    a[0] = 4
    print(a)

l = [1, 2]
test2(l)
print(l)

a = [1, 2]
print(a)
a[0] = 4
print(a)

# 18.4.7
import math
def extendList
