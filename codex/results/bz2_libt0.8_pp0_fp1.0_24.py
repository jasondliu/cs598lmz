import bz2
bz2.decompress(encode_data)

#
# 解压
with bz2.BZ2File('bz2.txt', 'wb') as f:
    f.write(encode_data)
print(open('bz2.txt', 'rb').read())
