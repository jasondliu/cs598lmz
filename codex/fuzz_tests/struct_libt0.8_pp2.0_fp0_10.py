import _struct
import _io

class class_type(_builtin_type):
    __qualname__ = 'class_type'
    _defaults = {}
    _attrs = []
    __slots__ = _attrs
    def __new__(cls, name, type_bases=(), class_dict={}):
        if not isinstance(type_bases, tuple):
            raise TypeError("type_bases must be a tuple")
        _tmp = class_dict.get('__doc__')
        if _tmp is None:
            class_dict['__doc__'] = None
        for att in cls._attrs:
            _tmp = class_dict.get(att)
            if _tmp is None:
                class_dict[att] = getattr(cls, '_defaults', {}).get(att)
        for att in class_dict._keys():
            if not isinstance(att, str):
                raise TypeError("Invalid attribute name {}".format(att))
            if att.startswith('__') and not att.endswith('__
