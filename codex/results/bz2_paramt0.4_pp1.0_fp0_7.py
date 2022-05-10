from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# 2. 压缩
import bz2
compressed = bz2.compress(data)

# 3. 压缩文件
with open('/tmp/example.bz2', 'wb') as f:
    f.write(compressed)

# 4. 解压缩文件
with open('/tmp/example.bz2', 'rb') as f:
    decompressed = bz2.decompress(f.read())
decompressed == data

# 5. 文件对象接口
import bz2
with open('/tmp/example.bz2', 'rb') as input:
    with bz2.open(input, 'rt') as decomp:
        for line in decomp:
            print(line)

# 6. 压缩率
import bz2
original = b'This is the original text.'
len(original)

compressed = bz2.compress(
