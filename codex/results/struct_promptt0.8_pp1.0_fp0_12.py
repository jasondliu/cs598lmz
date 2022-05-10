import _struct
# Test _struct.Struct

# Test the string constructor
S = _struct.Struct('P')
S.size == _struct.calcsize('P')
S = _struct.Struct('i')
S.size == _struct.calcsize('i')
S = _struct.Struct('ii')
S.size == _struct.calcsize('ii')
S = _struct.Struct('12s')
S.size == _struct.calcsize('12s')
S = _struct.Struct('16p')
S.size == _struct.calcsize('16p')
S = _struct.Struct('16P')
S.size == _struct.calcsize('16P')

try:
    _struct.Struct('p')
except _struct.error, msg:
    pass
else:
    raise RuntimeError, 'p not supported'

try:
    _struct.Struct('P')
except _struct.error, msg:
    raise RuntimeError, 'P not supported'

try:
    _struct.Struct('*')
except _struct.error, msg:
    pass
else
