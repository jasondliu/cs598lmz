import ctypes
# Test ctypes.CFUNCTYPE() prototype object
AddParams = ctypes.CFUNCTYPE(ctypes.c_uint, ctypes.c_char_p, ctypes.c_char_p)
# Test ctypes.CFUNCTYPE() prototype object
AddStrParams = ctypes.CFUNCTYPE(ctypes.c_uint,
    ctypes.c_char_p, ctypes.c_char_p)
# Call a Python function by address
AddByAddr = AddStrParams(AddStrParamsPtr)
AddByAddr(b"Hello Python", b" The Demon")
"""
现在，我们向Python添加一个新的C语言，并通过指针来访问它。请注意，因为我们
必须在C语言中使用一个C密钥字，因此没
