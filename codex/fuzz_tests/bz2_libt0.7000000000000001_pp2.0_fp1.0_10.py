import bz2
bz2_comp = bz2.BZ2Compressor()
with open("../data/sample.bz2", "wb") as f:
    for data in data_source:
        rv = bz2_comp.compress(data)
        if rv:
            f.write(rv)
    f.write(bz2_comp.flush())

# 解压缩
import bz2
with open("../data/sample.bz2", "rb") as f:
    file_content = f.read()
    
bz2_decomp = bz2.BZ2Decompressor()
uncompressed_data = bz2_decomp.decompress(file_content)
uncompressed_data

# 压缩后的文件小于原文件
import os
os.path.getsize("../data/sample.bz2")
# 1345
os.path.getsize("../data/sample.txt")
# 1487

# 压
