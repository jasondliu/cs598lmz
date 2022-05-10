import ctypes
ctypes.cast(id(d), ctypes.py_object).value

import sys
hex(id(d))
print(sys.getrefcount(d))

s = set([1,2,3])
print(sys.getrefcount(d))

import ctypes
def ref_count(address: int):
    return ctypes.c_long.from_address(address).value

print(ref_count(id(s)))

def ref_count(address):
    return ctypes.c_long.from_address(address).value

s = set([1,2,3])
r = ref_count(id(s)) 
r

def ref_count(address):
    return ctypes.c_long.from_address(address).value

s = set([1,2,3])
d = {}

print(ref_count(id(s)))
print(ref_count(id(d)))

d.update({s: 'set'})
print(ref_count(id(s))) 
print(ref_count(id(d)))


