import _struct
# Test _struct.Struct's methods with various input types
import _struct

# Verify that pack refuses to use a format string containing ' '
try:
    _struct.Struct('QI ').pack(1, 2)
except Exception as msg:
    print(msg)

# Verify that pack refuses to use a format string containing 'x'
try:
    _struct.Struct('QIx').pack(1, 2)
except Exception as msg:
    print(msg)

# Verify that pack refuses to use the standard size descriptor 'P'
try:
    _struct.Struct('QIP').pack(1, 2)
except Exception as msg:
    print(msg)

# Verify that pack refuses to accept the wrong number of arguments
try:
    _struct.Struct('QI').pack(1, 2, 3)
except Exception as msg:
    print(msg)

# Verify that pack refuses to accept a string argument for 's'
try:
    _struct.Struct('s').pack('ab')
except Exception as msg:
    print(msg)

# Verify that unpack refuses to accept the wrong number
