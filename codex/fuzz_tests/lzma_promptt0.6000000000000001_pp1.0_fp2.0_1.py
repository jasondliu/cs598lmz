import lzma
# Test LZMADecompressor 
with lzma.open('users.csv.xz') as f:
    file_content = f.read()

print(file_content[:10])

# Test LZMACompressor 
with lzma.open('users.csv.xz', 'w') as f:
    f.write(file_content)

print(file_content[:10])

# Test LZMADecompressor.readinto() 
with lzma.open('users.csv.xz') as f:
    data = f.read()
    print(data[:10])
    data = bytearray(len(data))
    f.readinto(data)
    print(data[:10])

# Test LZMADecompressor.seek() and LZMADecompressor.tell() 
with lzma.open('users.csv.xz') as f:
    print(f.tell())
    f.seek(10)
    print(f.tell())
    print(f.read(10))

# Test
