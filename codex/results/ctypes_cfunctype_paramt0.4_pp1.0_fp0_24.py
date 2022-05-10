import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)

def my_callback(x, y, button, pressed, modifiers, timestamp):
    print("(%d, %d) %s %s %s %d" % (x, y, "pressed" if pressed else "released", "ctrl" if modifiers & 1 else "", "shift" if modifiers & 2 else "", timestamp))

callback = FUNTYPE(my_callback)

if not lib.mouse_init(callback):
    print("Failed to initialize mouse")
    exit(1)

print("Press Ctrl+C to exit")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass

lib.mouse_cleanup()
</code>
Output:
<code>$ ./mouse_example 
(8, 6) pressed  1588553764
(8, 6) released  1588553764
(8, 6) pressed 
