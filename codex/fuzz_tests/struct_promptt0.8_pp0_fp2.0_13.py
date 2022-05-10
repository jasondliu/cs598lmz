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
tests = [
    ("b", 12, b'\x0c', None),
    ("b", -12, b'\xf4', None),
    ("B", 12, b'\x0c', None),
    ("B", 245, b'\xf5', None),
    ("h", 12, b'\x00\x0c', None),
    ("h", -12, b'\xff\xf4', None),
    ("H", 12, b'\x00\x0c', None
