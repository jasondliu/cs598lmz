import _struct

class _CDataMeta(type):
    def __new__(cls, name, bases, dct):
        if '_fields_' in dct:
            dct['_fields_'] = tuple(dct['_fields_'])
            for tp, name in dct['_fields_']:
                if isinstance(tp, str):
                    tp = _struct.__dict__[tp]
                if not isinstance(tp, _CDataMeta):
                    raise TypeError("invalid field type")
                dct[name] = property(operator.itemgetter(1), operator.setitem(1))
        return type.__new__(cls, name, bases, dct)

class _CData(object):
    __metaclass__ = _CDataMeta

    def __init__(self, *args):
        if len(args) > len(self._fields_):
            raise TypeError("too many arguments")
        self._buffer = bytearray(self._size)
        for name, val in zip(self._fields_,
