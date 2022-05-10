import _struct
# Test _struct.Struct with non-native endianness.
# XXX: This is not portable.
with _struct.Struct('>H') as st:
    print(st.unpack_from(b'\x00\x01'))
# XXX: This is portable, but not easily readable.
with _struct.Struct('>H') as st:
    print(st.unpack_from(b'\x00\x01'))
with _struct.Struct('@H') as st:
    print(st.unpack_from(b'\x00\x01'))
with _struct.Struct('=H') as st:
    print(st.unpack_from(b'\x00\x01'))
with _struct.Struct('<H') as st:
    print(st.unpack_from(b'\x00\x01'))
# Test _struct.Struct with non-native alignment.
with _struct.Struct('=H') as st:
    print(st.unpack_from(b'\x00\x01\x02'))
