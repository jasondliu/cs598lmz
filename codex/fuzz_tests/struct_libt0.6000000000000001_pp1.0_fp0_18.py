import _struct

def _get_struct(endianness, type_name):
    """Returns the struct format string for the given endianness and type_name.
    """
    return _struct.Struct(endianness + type_name)

def _get_pack_string(endianness, type_name):
    """Returns the pack string for the given endianness and type_name.
    """
    return endianness + type_name

def _unpack_from(file_object, endianness, type_name):
    """Unpacks a type from the file_object and returns it.

    Uses the given endianness and type_name to unpack the type from the
    file_object.
    """
    struc = _get_struct(endianness, type_name)
    return struc.unpack_from(file_object.read(struc.size))[0]

def _unpack_from_file(file_object, endianness, type_name):
    """Unpacks file_object and returns it.

    Uses the given endianness and
