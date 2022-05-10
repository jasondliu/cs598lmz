import ctypes
# Test ctypes.CField
ctypes.c_short.s
ctypes.c_short.b
# Test ctypes.Structure.from_address
a = ' ' * ctypes.sizeof(ctypes.c_int)
ctypes.c_int.from_address(id(a))
# Test ctypes.Union.from_address
a = ' ' * ctypes.sizeof(ctypes.c_int)
ctypes.c_int.from_address(id(a))
# Test ctypes.create_string_buffer
a = ctypes.create_string_buffer("Hello", size=10)
a.value
len(a)
# Test ctypes.c_buffer
# ctypes.c_buffer("Hello", 10)
# Test ctypes.c_wchar_p
ctypes.c_wchar_p("Hello")
a = ctypes.c_wchar_p("Hello")
a.value
len(a)
ctypes.c_wchar_p("Hello").value
ctypes.cast(ctypes.c_wchar_p("Hello"), ctypes.c
