from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(x)

# 使用gzip压缩数据
import gzip
s = b'witch which has which witches wrist watch'
len(s)
t = gzip.compress(s)
len(t)
gzip.decompress(t)
gzip.open('somefile.gz', 'rb')
gzip.open('somefile.gz', 'wt')
gzip.open('somefile.gz', 'wb')

# 使用zip文件
import zipfile
with zipfile.ZipFile('myzip.zip', 'w') as zf:
    zf.write('spam.txt')
    zf.write('eggs.txt')

with zipfile.ZipFile('myzip.zip') as zf:
    print(zf.namelist())
    spam_info = zf.getinfo('spam.txt')
    print(spam_info.file_size)
    print(spam_info.compress_size)
    print('Compressed file is
