import _struct

# This is a simple wrapper around the struct module.
# It provides a simple interface to pack/unpack
# data into binary format.
#
# It also provides a function to convert a string
# into a list of bytes.
class Packer:
    def __init__(self, endianness='little'):
        self.endianness = endianness

    def pack(self, format, *args):
        return _struct.pack(self.endianness + format, *args)

    def unpack(self, format, data):
        return _struct.unpack(self.endianness + format, data)

    def unpack_from(self, format, data, offset):
        return _struct.unpack_from(self.endianness + format, data, offset)

    def bytes_to_list(self, data):
        return list(data)

    def list_to_bytes(self, data):
        return bytes(data)
