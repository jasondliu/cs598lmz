import _struct
# Test _struct.Struct.__setstate__().
import _struct
import pickle

# Create an instance of Struct.
Struct = _struct.Struct("b")

# Create a pickle.
pickled = pickle.dumps(Struct)

# Recreate the pickle.
Struct = pickle.loads(pickled)

# Check that the recreated pickle is a Struct.
print(isinstance(Struct, _struct.Struct))

# Check that the recreated pickle is the correct Struct.
print(Struct.format)
