import ctypes
# Test ctypes.CFUNCTYPE

func = ctypes.CFUNCTYPE(ctypes.c_double)(lambda x: x+1)
for arg in [ctypes.c_double(1.0), 1.0]:
    print(func(arg))

func = ctypes.CFUNCTYPE(None, ctypes.c_char_p)(lambda x: print(x))
for arg in [b'Hello, World!', 'Hello, World!']:
    func(arg)

func = ctypes.CFUNCTYPE(None, ctypes.c_char_p)()
func()

func = ctypes.CFUNCTYPE(None)()
func()


# Test ctypes.PYFUNCTYPE

func = ctypes.PYFUNCTYPE(ctypes.c_double)(lambda x: x+1)
for arg in [ctypes.c_double(1.0), 1.0]:
    print(func(arg))

func = ctypes.PYFUNCTYPE(None, ctypes.c_char_p)(lambda x: print
