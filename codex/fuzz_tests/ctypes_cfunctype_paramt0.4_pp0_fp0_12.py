import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(x, y, button, pressed):
    print("Clicked at", x, y, "with button", button, "pressed" if pressed else "released")

my_callback_type = FUNTYPE(my_callback)

# Register the callback.
lib.register_callback(my_callback_type)

# Press any key to exit.
print("Press any key to exit.")
try:
    result = lib.do_main_loop()
    if result != 0:
        raise Exception("Failed with error code %s" % result)
finally:
    lib.unregister_callback()
</code>

