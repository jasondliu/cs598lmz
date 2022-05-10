from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# bz2_data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
# print(bz2.decompress(bz2_data))

# 打开压缩文件
with bz2.BZ2File('file.bz2', 'rb') as input:
    with open('file.txt', 'wb') as output:
        shutil.copyfileobj(input, output)

import gzip
# gzip.compress(bytes([1, 2, 3]))
# gzip.decompress(gzip.compress(bytes([1, 2, 3])))

# with gzip.open('file.gz', 'rt') as input:
#     print
