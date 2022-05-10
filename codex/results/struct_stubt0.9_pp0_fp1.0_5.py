from _struct import Struct
s = Struct.__new__(Struct)
#add new method
setattr(Struct, '__call__', Struct.__init__)


def _is_endian(c):
    """check is little/big endian"""
    #simplier & faster
    return c in '<>!'

def _calc_size(format):
    """calc size of struct data"""
    size = s.size
    s.__init__(format)
    return size

def _calcsize(format):
    """calc size of struct data using python routine"""
    return s.calcsize(format)

def _fill_format(format):
    """fills '0' after 'P'"""
    format = list(format)
    try:
        i = format.index('P')
        if i != len(format) - 1:
            format[i+1] = '0'
            _fill_format(''.join(format))
    except ValueError:
        pass
    else:
        return ''.join(format)
    return format

def _filter_format(format):

