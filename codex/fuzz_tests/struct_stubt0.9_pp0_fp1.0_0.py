from _struct import Struct
s = Struct.__new__(Struct)
s.__dict__.update(dict(format='I 2s f', size=14, alignment=4, pack=<built-in method pack of _struct.Struct object at 0xb7e89084>, pack_into=<built-in method pack_into of _struct.Struct object at 0xb7e89084>, unpack=<built-in method unpack of _struct.Struct object at 0xb7e89084>, unpack_from=<built-in method unpack_from of _struct.Struct object at 0xb7e89084>))
>>> dump(s, filter=lambda k, v: not k.startswith('_'))
_Struct__clearcache = <built-in method __clearcache__ of _struct.Struct object at 0xb7e89084>
_Formatter = <type '_Formatter'>
__doc__ = 'Compiled struct object'
__metaclass__ = <type 'type'>
__module__ = '_struct'
alignment = 4
format = 'I 2s f'
format_length_prefix = 'I'
