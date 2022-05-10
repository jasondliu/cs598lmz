import ctypes
ctypes.cast(0, ctypes.py_object)

# SEGV

# ____________________________________________________________

def test_py_object_from_address():
    import ctypes
    ctypes.py_object.from_address(0)

# SEGV

# ____________________________________________________________

def test_py_object_from_address_with_gc():
    import ctypes
    ctypes.py_object.from_address(0)

# SEGV

# ____________________________________________________________

def test_py_object_from_address_with_gc_and_del():
    import ctypes
    ctypes.py_object.from_address(0)

# SEGV

# ____________________________________________________________

def test_py_object_from_address_with_gc_and_del_and_del():
    import ctypes
    ctypes.py_object.from_address(0)

# SEGV

# ____________________________________________________________

