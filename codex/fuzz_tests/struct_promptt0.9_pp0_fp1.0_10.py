import _struct
# Test _struct.Struct
packer = _struct.Struct("I 10s f")
packed = packer.pack(123, b"My String", 3.14159)
print(packed)
# Batch unpacking
unpacker = _struct.Struct("I 10s f")
unpacker.size == packer.size
for value in unpacker.unpack(packed):
    print(value)

# Test struct.Struct
packer = struct.Struct("I 10s f")
packed = packer.pack(123, b"My String", 3.14159)
print(packed)
# Batch unpacking
unpacker = struct.Struct("I 10s f")
unpacker.size == packer.size
for value in unpacker.unpack(packed):
    print(value)

# -----
# formats
# -----

# Template | C Type | Python Type | Standard size | Standard alignment|
# --------- | ------ | ----------- | ------------- | ----------------- |
