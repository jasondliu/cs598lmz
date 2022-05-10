import _struct
# Test _struct.Struct<...> formatting.

struct = _struct.Struct('@P')
print struct.format
print struct.format_token
print struct.format_token('P')
print struct.alignment
print struct.size
print struct.__getattribute__('format')
print struct.__getattribute__('__dict__')

try:
    struct.format = 'i'
except AttributeError, msg:
    print msg

try:
    struct.__dict__
except AttributeError, msg:
    print msg

print repr(struct.pack(1))
print repr(struct.unpack(struct.pack(1)))
print repr(struct.unpack_from(struct.pack(1), 0))

print repr(struct.pack(2, 3))

try:
    struct.pack()
except TypeError, msg:
    print msg

try:
    struct.pack(1, 2)
except TypeError, msg:
    print msg
print repr(struct.unpack('\0'*8))
try:
    struct.unpack('\0'*7
