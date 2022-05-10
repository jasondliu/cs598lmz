import _struct
import _struct_helper

def _pack_into(fmt, buffer, offset, *args):
    size = _struct.calcsize(fmt)
    return _struct.pack_into(fmt, buffer, offset, *args)

def _unpack_from(fmt, buffer, offset):
    return _struct.unpack_from(fmt, buffer, offset)

def _pack(fmt, *args):
    return _struct.pack(fmt, *args)

def _unpack(fmt, buffer):
    return _struct.unpack(fmt, buffer)

def _unpack_int(buffer, offset, size):
    return _struct_helper.unpack_int(buffer, offset, size)

def _pack_int(number, size):
    return _struct_helper.pack_int(number, size)

def _unpack_float(buffer, offset, size):
    return _struct_helper.unpack_float(buffer, offset, size)

def _pack_float(number, size
