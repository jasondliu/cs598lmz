import ctypes
# Test ctypes.CFUNCTYPE is being handled correctly
# This test was generated from following C code
#   int f1(int* i) {
#     for (int j = 0; j < 10; j++)
#       *i = *i + j;
#   }
#   int f2(int* i) {
#     return *i * 2;
#   }
#   int main(void) {
#     int i = 1;
#     f1(&i);
#     f2(&i);
#   }

i_tp = ctypes.POINTER(ctypes.c_int)
f1 = ctypes.CFUNCTYPE(None, i_tp)
f2 = ctypes.CFUNCTYPE(ctypes.c_int, i_tp)

def run(func, f1, f2):
    i = ctypes.c_int()
    i.value = 1
    f1(i)
    func(f2(i))

run(llop.debug_print, f1(3), f2(3))


# test that multiple
