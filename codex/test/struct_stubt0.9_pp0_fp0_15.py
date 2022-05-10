from _struct import Struct
s = Struct.__new__(Struct)


# -- Extension Maps -----------------------------------------------------------

class _ExtensionMetadata(object):

    def __init__(self, name, struct_format,
                       struct_format_little_endian,
                       struct_format_big_endian):
        self.name = name
        self.struct_format = struct_format
        self.struct_format_little_endian = struct_format_little_endian
        self.struct_format_big_endian = struct_format_big_endian


class _ExtensionMap(object):

    @classmethod
    def register(cls, ext_type, name, struct_format,
                                    struct_format_little_endian,
                                    struct_format_big_endian):
        if cls.__index is None:
            raise TypeError('__index is not set on _ExtensionMap')

        index = len(cls.__index) + 1
        if index > 0xFF:
            raise ValueError('too many extensions registered')
        # The index of negative zero == 0
