import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int.in_dll(ctypes, 'x')

S.x

S.x = 1

S.x

ctypes.c_int.in_dll(ctypes, 'x').value

ctypes.c_int.in_dll(ctypes, 'y')

ctypes.c_int.in_dll(ctypes, 'y').value = 5

ctypes.c_int.in_dll(ctypes, 'y').value

ctypes.c_int.in_dll(ctypes, 'x').value

ctypes.c_int.in_dll(ctypes, 'x').value = 3

ctypes.c_int.in_dll(ctypes, 'x').value

S.x

S.x += 1

S.x

ctypes.c_int.in_dll(ctypes, 'x').value

ctypes.c_int.in_dll(ctypes, 'x').value = 3

ctypes.c_int.in_dll(ctypes, 'x').
