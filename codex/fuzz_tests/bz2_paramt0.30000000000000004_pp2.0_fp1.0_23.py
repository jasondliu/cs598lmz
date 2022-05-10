from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# %%
# 使用压缩文件
import bz2
with bz2.open('example.bz2', 'rt') as f:
    text = f.read()

# %%
# 压缩数据
import bz2
uncompressed_data = b'Hello World! Hello World! Hello World! Hello World!'
compressed_data = bz2.compress(uncompressed_data)
compressed_data

# %%
# 解压缩数据
bz2.decompress(compressed_data)

# %%
# 压缩文件
import bz2
with open('example.txt', 'rt') as input:
    with bz2.open('example.bz2', 'wt') as output:
        output.write(input.read())

# %%
# 解压缩文件
import bz2
with bz2.
