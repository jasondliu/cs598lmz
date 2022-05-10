import _struct

LittleEndianDataStream = _struct.Struct("!I")
BigEndianDataStream = _struct.Struct("!>I")


def decode_float32(v, stream=LittleEndianDataStream):
    return struct.unpack("!f", stream.pack(v))[0]


def decode_float64(v, stream=LittleEndianDataStream):
    return struct.unpack("!d", stream.pack(v))[0]


#
# baseFieldSet
#
class _baseFieldSet(object):

    def __init__(self, fields, endianness,
                 extra_field_setter=None):
        self._endianness = endianness
        self._fields = fields
        self._extra_field_setter = extra_field_setter

    def _set_field(self, dct, name, value, field):
        fname = field.name
        if fname == '':
            return value
