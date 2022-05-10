from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

decompressor = LZMADecompressor()
decompressed_data = decompressor.decompress(data)
print("Decompressed: {0} bytes".format(len(decompressed_data)))

data = b'\x00\x00\x00\x00\x00\x01\xff\xff'
with LZMADecompressor() as decompressor:
    decompressed_data = decompressor.decompress(data)

def blocks(input, blocksize):
    for i in range(0, len(input), blocksize):
        yield input[i : i + blocksize]

with open("enwik8", "rb") as input, LZMADecompressor() as decompressor:
    for block in blocks(input.read(), 1000000):
        decompressor.decompress(block)
print("Decompressed: {0} bytes".format(decompressor.unconsumed_tail))

with open("enwik8", "rb") as input, open("enwik8.decompressed
