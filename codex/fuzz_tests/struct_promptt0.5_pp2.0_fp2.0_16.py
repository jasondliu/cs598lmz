import _struct
# Test _struct.Struct

# Test _struct.Struct.__init__
try:
    _struct.Struct()
except TypeError:
    pass
else:
    print('_struct.Struct() should raise TypeError')

try:
    _struct.Struct('')
except ValueError:
    pass
else:
    print('_struct.Struct("") should raise ValueError')

try:
    _struct.Struct('@')
except ValueError:
    pass
else:
    print('_struct.Struct("@") should raise ValueError')

try:
    _struct.Struct('@I')
except ValueError:
    pass
else:
    print('_struct.Struct("@I") should raise ValueError')

try:
    _struct.Struct('@I I')
except ValueError:
    pass
else:
    print('_struct.Struct("@I I") should raise ValueError')

try:
    _struct.Struct('@I I ')
except ValueError:
    pass
else:
    print('_struct.Struct("@I I ") should raise Value
