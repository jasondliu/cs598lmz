import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def hello_world(arg):
    print("hello world")
    return 0
func = FUNTYPE(hello_world)
func(0)

### https://github.com/DarkNe/fun-with-python
