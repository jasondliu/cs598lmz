import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p)

def py_callback(message):
    print("Called back with message: " + message.decode("utf-8"))

print("Installing callback...")
c_callback = FUNTYPE(py_callback)
lib.install_callback(c_callback)
print("Callback installed.")

print("Asking C code to call it...")
lib.call_callback()
print("Called.")
</code>

