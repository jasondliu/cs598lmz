from _struct import Struct
s = Struct.__new__(Struct)
s.__setattr__('format', 'I 2s f')
s.__setattr__('size', 16)
s.__setattr__('_u', 'I 2s f')
s.__setattr__('_fmt', '=I 2s f')
s.__setattr__('_pack_', <built-in method pack_into of _struct.Struct object at 0x7f2cd8c1e6c0>)
s.__setattr__('_unpack_', <built-in method unpack_from of _struct.Struct object at 0x7f2cd8c1e6c0>)
s.__setattr__('_pack', <built-in method pack of _struct.Struct object at 0x7f2cd8c1e6c0>)
s.__setattr__('_unpack', <built-in method unpack of _struct.Struct object at 0x7f2cd8c1e6c0>)
s.__setattr__('format_char', 'I')
s.__setattr__('format_re', re.
