import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressed_data = decompressor.decompress(compressed_data)
# Test BZ2File
with bz2.BZ2File('data/sample.bz2', 'rb') as input:
    for line in input:
        print(line)

# Test LZMA Compressor
import lzma
compressed = lzma.compress(b'This is a test')
decompressed = lzma.decompress(compressed)
print(compressed)
print(decompressed)

# Test LZMAFile
with lzma.open('data/sample.xz', 'rb') as input:
    for line in input:
        print(line)

# Test zipfile
import zipfile
with zipfile.ZipFile('data/example.zip', 'r') as z:
    print(z.namelist())
    for name in z.namelist():
        print(z.getinfo(name))
    print(z.read('README.txt'
