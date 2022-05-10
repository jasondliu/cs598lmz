import _struct
# Test _struct.Struct constructor with keyword arguments
_struct.Struct(format='xyzzy')
_struct.Struct(format='xyzzy', byteorder='>')
_struct.Struct(format='xyzzy', byteorder='<')
_struct.Struct(format='xyzzy', byteorder='=')
# Test packing a struct with keyword arguments to the pack methods
_struct.Struct(format='xyzzy').pack(x=0, y=1, z=2, zz=3)
_struct.Struct(format='xyzzy', byteorder='>').pack(x=0, y=1, z=2, zz=3)
_struct.Struct(format='xyzzy', byteorder='<').pack(x=0, y=1, z=2, zz=3)
_struct.Struct(format='xyzzy', byteorder='=').pack(x=0, y=1, z=2, zz=3)
# Test unpack_into with keyword arguments
data = bytes(range(8))
