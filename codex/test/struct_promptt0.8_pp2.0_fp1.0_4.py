import _struct
# Test _struct.Struct
import _struct as struct

# ##########################################################################
# ## Functions
# ##########################################################################
def _bytes(n, obj=None):
    """Return the bytes object for the given object or integer.

    This function is useful for hashing binary datatypes that should be
    treated as a sequence of bytes.  For example, the network and
    "capsule digest" representations of IP addresses should be treated
    as sequences of 16 bytes.

    """
    if obj is not None:
        obj = int(obj)
    return _struct.Struct('!%dB' % (n,)).pack(obj)

def _pad(n, s):
    """Pad the given string to the given length n.

    The padding is done with null bytes.

    """
    return s + b"\x00" * (n - len(s))

