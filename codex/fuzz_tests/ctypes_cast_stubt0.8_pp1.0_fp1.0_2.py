import ctypes
ctypes.cast(0, ctypes.c_void_p).value
 
# %%
ctypes.c_int.from_address(10)
 
# %%
class A(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]
a = A.from_address(10)
a.a
 
# %%
import os
import mmap
with open("data.txt", "wb") as fout:
    fout.write(b"\x00" * 4096)
with open("data.txt", "r+b") as fin:
    mem = mmap.mmap(fin.fileno(), 0)
mem[0:4] = b"\xff\xff\xff\xff"
mem.seek(0)
list(mem)
 
# %%
import ctypes
libc = ctypes.cdll.LoadLibrary("libc.so.6")
libc.malloc(8)
ctypes.cast(libc.malloc(8), ctypes.POINTER(ctypes.c_int))
 
# %%
