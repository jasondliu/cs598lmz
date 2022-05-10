import _struct
# Test _struct.Struct objects with many format codes
#
# This just tests that the _struct module doesn't crash.
# Doesn't make any tests of the actual packed data.
try:
    struct_intern
except NameError:
    struct_intern = struct.Struct._intern

num_codes = 1000
codes = ''.join([random.choice(struct.__all__[10:])
                 for i in range(num_codes)])
fmt = '<' + codes
s = struct_intern(fmt)
s.size
s = struct.Struct(fmt)
s.size
s = struct_intern(('>' + codes).encode('ascii'))
s.size
s = struct.Struct(('>' + codes).encode('ascii'))
s.size
print(num_codes, "format codes")
