from types import FunctionType
a = (x for x in [1])
b = (x for x in [1])
print(a is b)
print(a == b)
print(type(a))
print(FunctionType)

#%%
import sys
sys.getrecursionlimit()
#%%
import ctypes
print(ctypes.c_int32)
print(ctypes.c_int32(1))
#%%
import sys
print(sys.platform)
print(sys.getwindowsversion())
print(sys.getrecursionlimit())
print(sys.getrefcount(1))
#%%
import array
a = array.array('i', [1, 2, 3])
print(a)
a.insert(1, 10)
print(a)
#%%
import math
x = math.pi
print(x)
print(math.floor(x))
print(math.ceil(x))
print(dir(math))
#%%
import urllib.request
with urllib.request.urlopen('https://www.python.org') as response:
    html = response.read()
    print(
