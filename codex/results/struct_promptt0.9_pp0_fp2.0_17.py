import _struct
# Test _struct.Struct
# First verify that it allocates the correct size
class S(tuple):
    def __new__(cls):
        return tuple.__new__(cls, (1,2))

# The size of a tuple is (n-1) * sizeof(PyObject *) and one for the size
tuple_size = _struct.calcsize("P" * 2)
assert _struct.calcsize(S) == tuple_size, (_struct.calcsize(S), tuple_size)

# The size of a dict with 5 items.
# Size of one dict entry is (size of key + size of value + index) * sizeof(PyObject *).
# Size of a dict is:
#
#   size of dict header
# + size of dict entry * dict fill factor (always 3/5 == 60%)
# + size of dict entry * dict fill factor % 2.
#
# Size of dict header is 2 * sizeof(PyObject *) for the allocation pointer of ma_values and ma_keys
# plus one for ma_used.
dict_size = 2 * _struct.calcsize("
