import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int)
CALLBACK_FUNCTION_NAME = "callback_function"
callback_function = FUNTYPE(lambda x: x * x)  # placeholder function

CallbackType = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)

# Define the callback type
@CallbackType
def mycallback(a, b):
    print("Python called with {} and {}".format(a, b))

so_file = os.path.join(os.getcwd(), "my_library.so")
foo = ctypes.CDLL(so_file)
foo.CALLBACK_FUNCTION_NAME = callback_function
foo.set_callback(Callbac
