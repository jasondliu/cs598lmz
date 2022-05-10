import _struct
# Test _struct.Struct('=i').pack(2**31)
# -2147483648 -> -2147483648
print _struct.Struct('=i').pack(2**31)
# Test _struct.Struct('=i').pack(-2**31)
# -2147483648 -> -2147483648
print _struct.Struct('=i').pack(-2**31)
# Test _struct.Struct('=i').pack(2**31-1)
# 2147483647 -> 2147483647
print _struct.Struct('=i').pack(2**31-1)
# Test _struct.Struct('=i').pack(-2**31+1)
# -2147483647 -> -2147483647
print _struct.Struct('=i').pack(-2**31+1)

print (_struct.Struct('=i').pack(_struct.Struct('=i').unpack(_struct.Struct('=i').pack(2**31))[0]))
print (_struct.Struct('=i').pack(_struct.Struct('=i').unpack(_struct.Struct
