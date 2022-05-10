import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
@FUNTYPE
def sine(x):
    return math.sin(x)
@FUNTYPE
def square(x):
    return x**2
ffi = FFI()
ffi.cdef("""
    double f(double);
""")

lib = ffi.dlopen("target/release/libembed.dylib")

t0 = time.time()
for i in range(1, 100):
    lib.f(i)
print(time.time() - t0)

print("load all:")

ffi = FFI()
ffi.cdef("""
    double sine(double);
    double square(double);
""")
lib = ffi.dlopen("target/release/libembed.dylib")

t0 = time.time()
for i in range(1, 100):
    lib.sine(i)
for i in range(1, 100):
    lib.square(i)
print(time.time() - t0)

print("load 1
