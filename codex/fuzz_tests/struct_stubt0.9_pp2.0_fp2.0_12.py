from _struct import Struct
s = Struct.__new__(Struct)
s.__setattr__("format", "I 2s f") # (format, *args, **kwargs)
s.__setattr__("size", s.calcsize())

# allow all to be set for debugging purposes, e.g.
# s.__setattr__("format", "ccc")

# **note**: defaults always allowed (even if not specified in the proto),
# and hence kwargs always allowed,
# but args must be specified before unpacking for compile-time checks
a, b, c = s.unpack(*vectors.S100(100))
print(a, b.decode(), c)

s1 = Struct.__new__(Struct)
s1.__setattr__("format", "I 2s") # (format, *args, **kwargs)
s1.__setattr__("size", s1.calcsize())

# allow all to be set for debugging purposes, e.g.
# s1.__setattr__("format", "ccc")

# **note**: defaults always allowed (even if not specified
