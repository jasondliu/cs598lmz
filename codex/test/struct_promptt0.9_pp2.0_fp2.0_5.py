import _struct
# Test _struct.Struct
try:
    _struct.Struct('xxxx')
except _struct.error as err:
    pass

# Test the _struct module's Symbols
symbols = dir(_struct)
for sym in ('Struct', 'error', 'pack', 'unpack'):
    assert sym in symbols

# Test the Struct Class
fmt = 'hhl'
s = _struct.Struct(fmt)
assert repr(s) == "Struct('hhl')"
assert isinstance(s, _struct.Struct)
assert s.format == fmt
assert len(s.unpack(s.pack(1, 2, 3))) == 3

# Set up the args, kwargs and format
args = (42,)
kwargs = {'format': 'l'}
fmt = 'hhh'

# Verify the unpacking and packing methods
#
# 1. Passing a format code string to pack_into() or unpack_from()
# 2. Passing a struct object to pack_into() or unpack_from() with a
#    format code string
format_string = 'hhl'
s
