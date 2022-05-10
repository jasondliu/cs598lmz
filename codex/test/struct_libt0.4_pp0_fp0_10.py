import _struct

#
# The following functions are used to create the
# "constants" used by the struct module.
#

def _make_int(name, value):
    return _struct.Struct(name + 'i').pack(value)

def _make_float(name, value):
    return _struct.Struct(name + 'd').pack(value)

def _make_complex(name, value):
    return _struct.Struct(name + 'd').pack(value.real) + \
           _struct.Struct(name + 'd').pack(value.imag)

#
# The following functions are used to create the
# "functions" used by the array module.
#

def _array_descr(name, typecode):
    return _array.array(name).typecode

def _array_fromstring(name, data):
    return _array.array(name, data)

def _array_tostring(name, a):
    return a.tostring()

def _array_fromunicode(name, data):
    return _
