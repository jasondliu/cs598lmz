import _struct
# Test _struct.Struct

# check that it's possible to override the pack and unpack methods
# (issue #9764)

class S(_struct.Struct):
    def pack(self, *args, **kwargs):
        return super().pack(*args, **kwargs)
    def unpack(self, *args, **kwargs):
        return super().unpack(*args, **kwargs)

s = S('i')
assert s.pack(42) == _struct.Struct('i').pack(42)
assert s.unpack(s.pack(42)) == (42,)
