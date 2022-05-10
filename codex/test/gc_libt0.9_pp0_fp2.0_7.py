import gc, weakref
from binascii import hexlify

#
# data entry
#


def get_data_name(data):
    if isinstance(data, numpy.lib.npyio.NpzFile):
        return data.fid.name
    if isinstance(data, numpy.ndarray):
        name = str(data)
        idx = name.index('0x')
        # sometimes the memory position has changed by now in which case we
        # get an error here
        try:
            name = hexlify(int(name[idx:]), 8)
        except (ValueError, TypeError):
            name = '-1'
        if isinstance(data, numpy.ma.core.MaskedArray):
            name += ' masked'
        return name
    name = str(data)
    typ = type(data)
    return name


# Additions by Peter Cock (1/2012)
