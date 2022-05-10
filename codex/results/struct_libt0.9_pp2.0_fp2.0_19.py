import _struct

unpack = _struct.unpack

sizeof = _struct.calcsize

c_int = _ctypes.c_int32
c_long = _ctypes.c_int32

c_float = _ctypes.c_float
c_double = _ctypes.c_double

# These are to avoid a case where os.path.splitext() would consider ''.py
# to be a valid module name.
_valid_magic = [_imp.get_magic()]
if _imp.get_tag() is not None:
    # We have a PEP 3147 tag.
    _valid_magic.append(_imp.get_tag() + _imp.get_magic())

# Helper to reverse a string.
_interning_dict = {}
def _reverse_dict(x):
    try:
        return _interning_dict[x]
    except KeyError:
        pass

    y = x[::-1]
    _interning_dict[x] = y
    return y

def _check_bytes_like(
