import _struct
# Test _struct.Struct with endianness.
print(_struct.Struct('=i').unpack(b'\0\0\0\42'))
# Test _struct.Struct without endianness.
print(_struct.Struct('i').unpack(b'\0\0\0\42'))
# Test _struct.Struct with a too large buffer.
_struct.Struct('ii').unpack(b'\0\0\0\0')
# Test that cycles in __reduce__() don't prevent pickling.
import pickle
assert pickle.loads(pickle.dumps(
    _struct.Struct('i'),
    protocol=pickle.HIGHEST_PROTOCOL))

# import _pickle

# Test __reduce__
# assert pickle.loads(pickle.dumps(
#   _pickle.Pickler,
#   protocol=pickle.HIGHEST_PROTOCOL)).__name__ == "Pickler"
# assert pickle.loads(pickle.dumps(
#   _pickle.Unpickler,
#   protocol=pickle
