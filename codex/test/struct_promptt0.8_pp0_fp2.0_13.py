import _struct
# Test _struct.Struct objects

try:
    import array
except ImportError:
    print('SKIP')
    raise SystemExit

if not hasattr(array, "array"):
    print('SKIP')
    raise SystemExit

# Test empty format string
try:
    _struct.Struct("")
except ValueError:
    print("ValueError")

# Test unsupported format string
try:
    _struct.Struct("xyz")
except ValueError:
    print("ValueError")

# Test basic packing
# fmt, value, big_endian, native_endian
