import lzma
# Test LZMADecompressor
data = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00'

compressor = decompressobj()

with open('sample.txt.xz', 'rb') as input, open('output.txt', 'wb') as output:
    while True:
        block = input.read(64 * 1024)
        if not block:
            break
        output.write(compressor.decompress(block))
    output.write(compressor.flush())

with lzma.open('sample.txt.xz') as f:
    file_content = f.read()
    print(file_content)
with lzma.open('sample.txt.xz') as f:
    for i in range(3):
        line = f.readline()
        print(line)
    f.seek(0)
    for i in range(2):

