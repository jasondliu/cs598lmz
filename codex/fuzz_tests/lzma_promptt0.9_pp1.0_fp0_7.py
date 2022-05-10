import lzma
# Test LZMADecompressor instance
cmp = lzma._lzma.LZMADecompressor()

try:
    cmp.decompress(data)
except EOFError:
    pass
else:
    print("Failed to raise EOFError")

cmp.flush()
cmp.unused_data
final_data = cmp.unused_data

final_data
print('Decompressed data is %d bytes' % len(final_data))
cmp = None

# This could be "Hello, world!" or a binary file, it doesn't matter.
with lzma.open('./backup/hello.xz', mode='w') as f:
    f.write(data)

with lzma.open('./backup/hello.xz') as f:
    file_content = f.read()

print(file_content)
