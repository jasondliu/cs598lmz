import ctypes
ctypes.cast(p,ctypes.py_object).value

print(type(p))
print(type(li))

li[0]
p[0]

p[1]
li[1]

type(li)

type(p)

p[3]

li[3]

type(li)

type(p)

import sys

sys.getrefcount(li)

sys.getrefcount(p)

sys.getrefcount(000)

p = None

sys.getrefcount(000)

import sys

sys.getrefcount(000)

import gc
gc.collect()

sys.getrefcount(000)

gc.collect()

sys.getrefcount(000)

gc.collect()

p = None

sys.getrefcount(000)

gc.collect()

sys.getrefcount(000)

a = []

sys.getrefcount(a)

import sys
gc.collect()

a = None

sys.getrefcount
