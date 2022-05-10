from _struct import Struct
s = Struct.__new__(Struct)
s.__init__("L")

def make_struct(format):
    return Struct.__new__(Struct)

def make_struct_unpack(format):
    return Struct.__new__(Struct)

def make_struct_pack(format):
    return Struct.__new__(Struct)

def make_struct_calcsize(format):
    return Struct.__new__(Struct)

def struct_unpack(format, buffer):
    return s.unpack(buffer)

def struct_pack(format, *args):
    return s.pack(*args)

def struct_calcsize(format):
    return s.size

# vim:set ts=8 sw=4 sts=4 tw=78 et:
