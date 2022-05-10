import ctypes
# Test ctypes.CField instance
assertCField(ctypes.CField, instance=ctypes.CField("name", ctypes.c_int),
             expected_name="name", expected_type=ctypes.c_int)

# Test namedtuple instance
assertCField(ctypes.CField, instance=ctypes.CField("name", ctypes.c_int),
             expected_name="name", expected_type=ctypes.c_int)

# Test it's subclass
class MyCField(ctypes.CField):
    pass

assertCField(type=MyCField, instance=MyCField("name", ctypes.c_int),
             expected_name="name", expected_type=ctypes.c_int)

# Negative tests
# No such attribute
try:
    assertCField(ctypes.CField, instance=ctypes.CField("name", ctypes.c_int),
                 expected_name="nam", expected_type=ctypes.c_int)
except AssertionError:
    pass
else:
    raise Exception("this should fail")


