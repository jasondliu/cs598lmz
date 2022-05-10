import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int(1)
ctl = ctypes.c_int
controller = S()

print("controller.x: ", controller.x)
print("type: ", type(controller.x))
print("isinstance(S.x, ctl): ", isinstance(S.x, ctl))
try:
    print("isinstance(controller.x, ctl): ", isinstance(controller.x, ctl))
except:
    print("Exception: cannot check isinstance(controller.x, ctl)")

