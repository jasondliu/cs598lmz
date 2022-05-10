import _struct
# Test _struct.Struct with non-native format
try:
    s = _struct.Struct('<I')
except _struct.error:
    pass
# Test _struct.Struct with non-native format
try:
    s = _struct.Struct('<I')
except _struct.error:
    pass
# Test _struct.Struct with native format
try:
    s = _struct.Struct('@I')
except _struct.error:
    pass
# Test _struct.Struct with native format
try:
    s = _struct.Struct('@I')
except _struct.error:
    pass
# Test _struct.Struct with non-native format
try:
    s = _struct.Struct('>I')
except _struct.error:
    pass
# Test _struct.Struct with non-native format
try:
    s = _struct.Struct('>I')
except _struct.error:
    pass
# Test _struct.Struct with native format
try:
    s = _struct.Struct('=I')
except _struct.error:
    pass
# Test _struct.Struct with native format
