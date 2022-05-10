import _struct
import math

def _is_big_endian(dtype):
    return ord(dtype.byteorder) == dtype.byteorder in (">", "|", "=")

def _init_numpy_registry():
    reg = {}
    _struct._registry = reg
    from numpy.core.multiarray import dtype
    for type_, kind in dtype.kind_dict.iteritems():
        if not kind.isalnum():
            # We cannot handle spaces
            continue
        if type_ in dtype.alignment_dict:
            alignment = dtype.alignment_dict[type_]
        else:
            alignment = 1
        fmt = ">" + kind
        dtype_ = numpy.dtype(type_)
        reg[dtype_] = _struct.Struct(fmt), alignment
    # Fill-up missing basic typdefs
    for kind in dtype.kind_dict.itervalues():
        if not kind.isalnum():
            # We cannot handle spaces
            continue
        if kind in reg:

