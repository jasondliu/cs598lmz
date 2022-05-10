import _struct

_pack_ = 1

class _hdr(Structure):
    _fields_ = [("magic", c_uint32),
                ("version", c_uint32),
                ("compressor", c_char * 4),
                ("blocksize", c_uint32)]

class _xattr(Structure):
    _fields_ = [("id", c_uint32),
                ("namelen", c_uint32),
                ("valuelen", c_uint32),
                ("name", c_char * 256),
                ("value", c_char)]

def _u16(string, offset):
    return _struct.unpack_from("<H", string, offset)[0]

def _u32(string, offset):
    return _struct.unpack_from("<I", string, offset)[0]

def _hdr_unpack(string):
    hdr = _hdr.from_buffer_copy(string)
    hdr.compressor = hdr.compressor.split("\0")[0]
    if hdr.compressor
