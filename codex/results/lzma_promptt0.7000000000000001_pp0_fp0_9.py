import lzma
# Test LZMADecompressor
with lzma.LZMADecompressor() as dec:
    with open('foo.xz', 'rb') as f:
        file_content = f.read()
    data = dec.decompress(file_content)

print(data)

# Test LZMACompressor
cmpr = lzma.LZMACompressor()
with open('foo.xz', 'wb') as f:
    f.write(cmpr.compress(b"Hello"))
    f.write(cmpr.flush())

# Test LZMAFile
with lzma.open('foo.xz', mode='rt') as f:
    file_content = f.read()
    print(file_content)

'''
输出：
Hello
Hello
'''


'''
bzip2
'''
import bz2

# Test BZ2Compressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\
