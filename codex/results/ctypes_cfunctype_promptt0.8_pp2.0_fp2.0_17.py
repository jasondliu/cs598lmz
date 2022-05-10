import ctypes
# Test ctypes.CFUNCTYPE
def print_int(i):
    print(i)
CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
cmp_func = CMPFUNC(print_int)
print(cmp_func)
print(cmp_func(5))
# Test ctypes.c_wchar_p
print('ctypes.c_wchar_p')
print(ctypes.sizeof(ctypes.c_wchar_p))
print(ctypes.sizeof('中国'))
s = ctypes.c_wchar_p('中国')
print('s:', s.value)
print('s:', s.value[0])
print('s:', s.value[1])
print('s:', s.value[2])
print('s:', len(s.value))
print('s:', s.value[3]) # Seg Fault
print(isinstance(s, ctypes.c_wchar_p))
print('s:', s.value[0])
print('s
