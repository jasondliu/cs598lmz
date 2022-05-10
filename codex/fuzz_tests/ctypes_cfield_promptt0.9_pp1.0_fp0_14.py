import ctypes
# Test ctypes.CField instance.
try:
    gdb.parse_and_eval("a_complex")
    a_complex = ctypes.CField("a_complex", gdb.lookup_type("complex").pointer())
    value = a_complex.get_value(ctypes.CUnexposedObject("a_complex", 100))
    if value.real != 10 or value.imag != 5:
        raise RuntimeError("CField: wrong value (%s)" % value)
except RuntimeError as ex:
    fail(ex)
else:
    pass
# Test ctypes.CField instance.
try:
    gdb.parse_and_eval("a_complex")
    a_complex = ctypes.CField(
            "a_complex",
            ctypes.CPointer(ctypes.CStructure(None, None, None, size=ctypes.sizeof(
                gdb.lookup_type("complex")))))
    value = a_complex.get_value(
            ctypes.CUnexposedObject("a_complex", 100,
                ctypes.CStructure(None, None,
