import _struct
# Test _struct.Struct
try:
    class foo : pass
    s = _struct.Struct()
except:
    print('SKIP')
    raise SystemExit

# Python C-API documentation shows that this should work.
# Struct.__new__(<class '_struct.Struct'>, ., ., . .)
try:
    s = _struct.Struct('b', 'c', 'h', 'i', 'l', 'f', 'd')
except:
    print('SKIP')
    raise SystemExit

print(s.format)
print(s.size)
print(s.pack(1, 2, 3, 4, 5, 6.5, 7.5))

print(s.unpack(s.pack(1, 2, 3, 4, 5, 6.5, 7.5)))

# Check some invalid formats
try:
    _struct.Struct('')
except struct.error:
    print('struct.error')

try:
    _struct.Struct('x')
except struct.error:
    print('struct.error')

# Very long format string

