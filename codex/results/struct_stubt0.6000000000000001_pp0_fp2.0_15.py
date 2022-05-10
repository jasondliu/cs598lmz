from _struct import Struct
s = Struct.__new__(Struct)
s.format = '<i'
s.size = 4
s.pack_into = lambda buf, offset, val: buf.write(pack('<i', val))

def _unpack(buf):
    return unpack('<i', buf.read(4))[0]

def _sizeof():
    return 4

def _offsetof(attr):
    return _cffi_field_offset(b'int', attr)

def _typeof():
    return _ffi.typeof('int')

_ffi.typeof('int')

_ffi.typeof('int').size

_ffi.typeof('int').alignment

_ffi.typeof('int').cname

_ffi.typeof('int').elements

_ffi.typeof('struct {int x;}').elements

_ffi.typeof('struct {int x;}').fields

_ffi.typeof('struct {int x;}').fieldnames

_ffi.typeof('struct {int x;}').has_var
