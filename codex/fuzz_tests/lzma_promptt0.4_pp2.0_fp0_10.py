import lzma
# Test LZMADecompressor
with lzma.open('data/enwik9.xz') as f:
    file_content = f.read()

print(file_content[:10])

# Test LZMACompressor
compressor = lzma.LZMACompressor()
with open('data/enwik9.xz', 'wb') as f:
    f.write(compressor.compress(file_content))
    f.write(compressor.flush())

# Test LZMAFile
with lzma.open('data/enwik9.xz') as f:
    file_content = f.read()

print(file_content[:10])

# Test LZMAError
try:
    with lzma.open('data/enwik9.xz') as f:
        file_content = f.read()
except lzma.LZMAError as e:
    print(e)

# Test is_check_supported
print(lzma.is_check_supported(lzma.CHECK_CRC64))

# Test
