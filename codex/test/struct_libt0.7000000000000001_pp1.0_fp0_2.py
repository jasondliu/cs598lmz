import _struct

#-----------------------------------------------------------------------
#Helper functions
#-----------------------------------------------------------------------
def _parse_flags(flags):
    if flags < 0:
        raise ValueError("Invalid flags argument: %r." % (flags))
    if flags > 0xff:
        raise ValueError("Invalid flags argument: %r." % (flags))
    return flags

def _parse_string(str):
    if type(str) is not str:
        raise TypeError("Invalid string argument: %r." % (str))
    return str

def _parse_address(addr):
    if not (type(addr) is Address):
        raise TypeError("Invalid address argument: %r." % (addr))
    return addr

def _parse_short_address(addr):
    if not (type(addr) is ShortAddress):
        raise TypeError("Invalid short address argument: %r." % (addr))
    return addr

def _parse_param(param):
    if type(param) is not int:
        raise TypeError("Invalid parameter argument: %r." % (param))
    if param < 0:
        raise
