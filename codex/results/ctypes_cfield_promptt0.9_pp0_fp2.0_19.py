import ctypes
# Test ctypes.CField object
if ctypes.sizeof(c_int) == ctypes.sizeof(c_long):
    class S(Structure):
        _fields_ = [("a", c_long),
                    ("b", c_int)]
else:
    class S(Structure):
        _fields_ = [("a", c_int),
                    ("b", c_int)]
    S._pack_ = 4
TestError(ctypes.CField.__repr__(S.a),
          "CField object 'a' of type <(class|type) '_ctypes.CField'>")

# Test ctypes.CField instance member
TestError(ctypes.memmove,
          "function 'memmove' not found")

# Test C instance member
test_keepref = ctypes.CFUNCTYPE(c_int, c_int)(lambda: 1)
tracemalloc.start()
snapshot = tracemalloc.take_snapshot()
c_int.__doc__
tracemalloc.stop()
top_stats = snapshot.filter_tr
