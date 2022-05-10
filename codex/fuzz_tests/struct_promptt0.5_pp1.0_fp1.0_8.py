import _struct
# Test _struct.Struct
print(_struct.Struct('i').size)
print(_struct.Struct('i').pack(42))
print(_struct.Struct('i').unpack(_struct.Struct('i').pack(42)))
# Test struct
print(struct.pack('i', 42))
print(struct.unpack('i', struct.pack('i', 42)))
# Test struct.Struct
print(struct.Struct('i').size)
print(struct.Struct('i').pack(42))
print(struct.Struct('i').unpack(struct.Struct('i').pack(42)))
# Test _struct.Struct.__dict__
print(sorted(_struct.Struct('i').__dict__.items()))
# Test struct.Struct.__dict__
print(sorted(struct.Struct('i').__dict__.items()))
# Test _struct.Struct.__dir__
print(sorted(_struct.Struct('i').__dir__()))
# Test struct.Struct.__dir__
print(sorted(struct.Struct('i').__dir__()))
