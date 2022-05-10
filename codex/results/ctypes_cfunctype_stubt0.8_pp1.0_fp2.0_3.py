import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 2
@FUNTYPE
def fun2():
    return (1, 2)

print fun()
print fun2()
record = ctypes.create_string_buffer(5)
record2 = ctypes.create_string_buffer(5)
print record[0]
print record.value
ctypes.memmove(record, 'xxxxx', 5)
ctypes.memmove(record2, 'xxxxx', 5)
print record.value
import ctypes
import os
def get_syscall_number(name):
    """
    Return the system call number for this function name in this
    architecture.
    """
    if not name.startswith("sys_"): name = "sys_" + name
    return getattr(ctypes.CDLL(None), name)()

open_syscall_number = get_syscall_number("open")
print open_syscall_number

libc = ctypes.cdll.LoadLibrary("libc.so.6")

libc.open.argtypes = (ctypes.c_char_p,ctypes
