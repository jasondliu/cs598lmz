import ctypes
# Test ctypes.CFUNCTYPE
def ptr_example(x):
    print x

ptr = ctypes.CFUNCTYPE(None, ctypes.c_int)(ptr_example)
print 'CFUNCTYPE', type(ptr), ptr
ptr(42)
print

# Test ctypes.c_char_p
print 'c_char_p', type(ctypes.c_char_p), ctypes.c_char_p
s = ctypes.c_char_p('Python')
print s.value, type(s.value)
s = ctypes.c_char_p(42)
print s.value, type(s.value)
print

# Test ctypes.c_wchar_p
print 'c_wchar_p', type(ctypes.c_wchar_p), ctypes.c_wchar_p
s = ctypes.c_wchar_p('Python')
print s.value, type(s.value)
s = ctypes.c_wchar_p(42)
print s.value, type(s.value)
print


