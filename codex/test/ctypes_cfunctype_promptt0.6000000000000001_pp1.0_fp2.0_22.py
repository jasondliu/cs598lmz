import ctypes
# Test ctypes.CFUNCTYPE

def callback(x, y):
    return x * y

CALLBACK = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# This is how you'd call the callback in C:
# int cb(int x, int y) {
#     return x * y;
# }
#
# int call_int_int_int(int(*cb)(int, int), int x, int y) {
#     return cb(x, y);
# }
#
# int main(void) {
#     return call_int_int_int(cb, 12, 34);
# }

lib = ctypes.CDLL(None)
