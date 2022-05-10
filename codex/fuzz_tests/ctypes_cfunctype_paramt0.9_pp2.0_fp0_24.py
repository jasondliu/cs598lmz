import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int64,ctypes.POINTER(ctypes.c_char),ctypes.c_int64)
str2chr = (FUNTYPE(LLIB.str2chr))
hijack_open = (FUNTYPE(LLIB.hijack_open))

test = "hello"
tlen = len(test)
tchar = ctypes.create_string_buffer(tlen+1)
tchar.value = test
print tchar.value
print tlen
str_type = ctypes.c_char_p
str_type_in = ctypes.POINTER(ctypes.c_char)
try:
    print(str2chr(tchar,ctypes.c_int64(tlen)))
except:
    print("except")
print hijack_open(ctypes.c_char_p("/tmp/migration_test"),ctypes.c_int64(0))

print("end")
