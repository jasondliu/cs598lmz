import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
p = ctypes.c_int.in_dll(ctypes.pythonapi, 'Py_IsInitialized')
py_is_initialized = FUNTYPE(p)

if py_is_initialized() == 0:
    print('Python not initialized')
    sys.exit(0)

# if Python is initialized, then we can import the modules
# and run the main function
from source import main
main()
