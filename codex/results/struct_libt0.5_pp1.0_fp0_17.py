import _struct

class _CDataMeta(type):
    _size_ = 0
    _length_ = 0
    _is_pointer_ = False
    _is_array_ = False
    _is_struct_ = False
    _fields_ = []
    _subtypes_ = []

    def __new__(cls, name, bases, dct):
        if '_type_' not in dct:
            raise TypeError('_type_ not defined in CData subclass')
        return type.__new__(cls, name, bases, dct)

    def __init__(cls, name, bases, dct):
        super(_CDataMeta, cls).__init__(name, bases, dct)
        cls._size_ = _ffi.sizeof(cls._type_)
        cls._length_ = _ffi.sizeof(cls._type_) / _ffi.sizeof(cls._type_.item)
        cls._is_pointer_ = cls._type_.kind == 'pointer'
        cls._is_array
