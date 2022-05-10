from _struct import Struct
s = Struct.__new__(Struct)

s.format = '<3si'
s.size = s.calcsize(s.format)

print(s.size)
print(s.pack(b'abc', 123))
print(s.unpack(b'abc\x00\x00\x00{'))
print(s.unpack_from(b'abc\x00\x00\x00{', 0))
print(s.unpack_from(b'abc\x00\x00\x00{', 1))

# Format   C Type          Python type         Standard size
#
# x        pad byte        no value
# c        char            bytes of length 1   1
# b        signed char     integer             1
# B        unsigned char   integer             1
# ?        _Bool           bool                1
# h        short           integer             2
# H        unsigned short  integer             2
# i        int             integer             4
# I        unsigned int    integer             4
# l        long            integer             4
# L        unsigned long   integer             4
# q        long long       integer            
