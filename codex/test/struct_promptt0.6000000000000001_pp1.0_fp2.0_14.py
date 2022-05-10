import _struct
# Test _struct.Struct
print(_struct.Struct('I').pack(123456789))
print(_struct.Struct('I').unpack(_struct.Struct('I').pack(123456789)))
print(_struct.Struct('I').unpack(_struct.Struct('I').pack(0xffffffff)))

import _testcapi
# Test _testcapi.INT_MAX
print(_testcapi.INT_MAX)

# Test _testcapi.UINT_MAX
print(_testcapi.UINT_MAX)

# Test _testcapi.LONG_MAX
print(_testcapi.LONG_MAX)

# Test _testcapi.ULONG_MAX
print(_testcapi.ULONG_MAX)

# Test _testcapi.INT_MIN
print(_testcapi.INT_MIN)

# Test _testcapi.LONG_MIN
print(_testcapi.LONG_MIN)

# Test _testcapi.INT_MAX + 1
print(_testcapi.INT_MAX + 1)

# Test _testcapi.LONG
