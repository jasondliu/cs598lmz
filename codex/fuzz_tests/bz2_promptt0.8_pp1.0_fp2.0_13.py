import bz2
# Test BZ2Decompressor
data = open(bz2.__file__, 'rb').read(100)
print(data)
print('length:', len(data))
print(bz2.decompress(data))

# 示例三
import bz2
# BZ2Decompressor 放入循环缓存
uncompressor = bz2.BZ2Decompressor()
with open(bz2.__file__, 'rb') as input:
    with open('bz2_decompress.txt', 'wb') as output:
        while True:
            block = input.read(1024)
            if not block:
                break
            output.write(uncompressor.decompress(block))

# 示例四
import bz2
# BZ2Compressor 放入循环缓存
compressor = bz2.BZ2Compressor()
with open('bz2_decompress.txt', 'rb') as input:
    with
