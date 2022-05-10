import lzma
# Test LZMADecompressor
bytes_in = b'\x00' * 1024
with lzma.LZMADecompressor() as dec:
    bytes_out = b''
    for block in iter(lambda: bytes_in, b''):
        bytes_out += dec.decompress(block)
assert bytes_out == b'\x00' * 1024

# Test LZMAFile
# compress level 1
with open('lzma_compression_test.txt', 'rb') as source:
    with lzma.LZMAFile(source, mode='w', preset=1) as target:
        pass
with open('lzma_compression_test.txt', 'rb') as source:
    with lzma.LZMAFile(source) as file:
        bytes_out = file.read()
assert bytes_out == b'This is a test.'
# compress level 6
with open('lzma_compression_test.txt', 'rb') as source:
    with lzma.LZMAFile(source, mode='w', preset=6) as target:
