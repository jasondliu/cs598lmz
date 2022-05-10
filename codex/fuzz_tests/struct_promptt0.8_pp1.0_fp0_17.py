import _struct
# Test _struct.Struct with a buffer
_struct.Struct('h').pack_into(b'\0'*2, 0, 1)
_struct.Struct('h').pack_into(b'\0'*2, 0, -1)
_struct.Struct('h').pack_into(b'\0'*2, 0, 2**15-1)
_struct.Struct('h').pack_into(b'\0'*2, 0, -(2**15))
_struct.Struct('h').pack_into(b'\0'*2, 0, 2**15)
_struct.Struct('h').pack_into(b'\0'*2, 0, -(2**15+1))
_struct.Struct('h').pack_into(b'\0'*2, 0, 2**31-1)
_struct.Struct('h').pack_into(b'\0'*2, 0, -(2**31))
_struct.Struct('h').pack_into(b'\0'*2, 0, 2**31)
_struct.Struct('h').pack_
