from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')

def _pack(format, *args):
    return s.pack(*args)

def _unpack(format, *args):
    return _struct.unpack(format, *args)

def _unpack_from(format, *args):
    return _struct.unpack_from(format, *args)

def _calcsize(format):
    return _struct.calcsize(format)

else:
    def _pack(format, *args):
        return _struct.pack(format, *args)

    def _unpack(format, *args):
        return _struct.unpack(format, *args)

    def _unpack_from(format, *args):
        return _struct.unpack_from(format, *args)

    def _calcsize(format):
        return _struct.calcsize(format)

#------------------------------------------------------------------------------#
# Structs                                                                      #
#------------------------------------------------------------------------------#
class BoolStruct(object):
    """
    Struct for serializing boolean values.
   
