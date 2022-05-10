import _struct
# Test _struct.Struct

# Test _struct.Struct.__new__

# Test _struct.Struct.__new__ with bad format
try:
    _struct.Struct('abc')
except ValueError:
    pass
else:
    print('_struct.Struct("abc") did not raise ValueError')

# Test _struct.Struct.__new__ with bad format
try:
    _struct.Struct('@')
except ValueError:
    pass
else:
    print('_struct.Struct("@") did not raise ValueError')

# Test _struct.Struct.__new__ with bad format
try:
    _struct.Struct('@abc')
except ValueError:
    pass
else:
    print('_struct.Struct("@abc") did not raise ValueError')

# Test _struct.Struct.__new__ with bad format
try:
    _struct.Struct('@i')
except ValueError:
    pass
else:
    print('_struct.Struct("@i") did not raise ValueError')

# Test _struct.Struct.__new__ with bad format
