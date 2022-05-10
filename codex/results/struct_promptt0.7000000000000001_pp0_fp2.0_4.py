import _struct
# Test _struct.Struct.format_map()
# bug 11812

fmt_map = {'unpack': 'h', 'pack': 'h', 'size': 2}

fmt = '=' + ''.join(fmt_map[x] for x in ('unpack', 'pack'))
s = _struct.Struct(fmt)
assert s.format == fmt
print(s)
try:
    s.format_map(fmt_map)
except TypeError as e:
    assert str(e) == "format_map() missing 1 required positional argument: 'self'"
else:
    raise AssertionError("Didn't raise TypeError")
