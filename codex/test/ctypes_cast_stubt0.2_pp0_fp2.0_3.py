import ctypes
ctypes.cast(0, ctypes.py_object)

# SEGV

# ____________________________________________________________

def test_ctypes_cast_2():
    import ctypes
    ctypes.cast(0, ctypes.c_int)

# SEGV

# ____________________________________________________________

def test_ctypes_cast_3():
    import ctypes
    ctypes.cast(0, ctypes.c_void_p)

# SEGV

# ____________________________________________________________

def test_ctypes_cast_4():
    import ctypes
    ctypes.cast(0, ctypes.c_char_p)

# SEGV

# ____________________________________________________________

def test_ctypes_cast_5():
    import ctypes
    ctypes.cast(0, ctypes.c_wchar_p)

# SEGV

# ____________________________________________________________

def test_ctypes_cast_6():
    import ctypes
    ctypes.cast(0, ctypes.c_char)

# SEGV

#
