import ctypes
ctypes.cast(100, ctypes.py_object).value

# Output: 100

ctypes.cast("abc\0abc\0"+("%0*x"%(0x8-20,"")), ctypes.py_object).value



# Output: 'abc\x00'

ctypes.cast("abc\0abc\0"+("%0*x"%(0x10-16,"")), ctypes.py_object).value


# Output: 'abc\x00abc\x00'

ctypes.cast("abc\0abc\0"+("%0*x"%(0x18-16,"")), ctypes.py_object).value



# Output: 'abc\x00abc\x00\xff\xff\xff\xffaaa'

Notice that in the last example the address size and the pointer length are not complying anymore. At this point,

ctypes.cast("abc\0abc\0"+("%0*x"%(0x18-16,"")), ctypes.py_object).value

returns a ctypes
