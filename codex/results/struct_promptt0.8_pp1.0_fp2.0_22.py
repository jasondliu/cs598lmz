import _struct
# Test _struct.Struct('i') with a buffer_info that has len > sizeof.
t = _struct.Struct('i')
f = t.pack_into
buf = bytearray(b"abcd")
f(buf, 0, 2)
f(buf, 1, 3)
assert buf == bytearray(b"\x02\x00\x00\x00\x03\x00\x00\x00")
# Test str.format_map with missing mapping keys.
import string
tmpl = string.Template('$who likes $what')
assert tmpl.substitute(who='tim') == 'tim likes $what'
import io
# Test io.BytesIO.read() after close.
b = io.BytesIO(b'abc')
b.close()
try:
    b.read()
except ValueError:
    pass
else:
    print('no exception')
# Test io.StringIO.read() after close.
b = io.StringIO('abc')
b.close()
try:
    b.read()
except ValueError:
    pass

