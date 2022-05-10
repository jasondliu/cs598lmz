import _struct
# Test _struct.Struct with integer types.                                    #

try:
    _struct.Struct('1').pack(1)
except error as err:
    print(err)

try:
    _struct.Struct('1').pack(1.0)
except error as err:
    print(err)

try:
    _struct.Struct('1p').pack(1)
except error as err:
    print(err)

try:
    _struct.Struct('1p').pack(1.0)
except error as err:
    print(err)

try:
    _struct.Struct('1P').pack(1)
except error as err:
    print(err)

try:
    _struct.Struct('1P').pack(1.0)
except error as err:
    print(err)

# Test _struct.Struct with float types.                                      #

try:
    _struct.Struct('1d').pack(1)
except error as err:
    print(err)

try:
    _struct.Struct('1d').pack(1.0)
