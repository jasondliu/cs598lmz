import lzma
lzma.decompress('test.xz')

# 使用gzip压缩
import gzip
s = b'witch which has which witches wrist watch'
with gzip.open('test.gz', 'wb') as f:
    f.write(s)
with gzip.open('test.gz', 'rb') as f:
    print(f.read())

# 使用bz2压缩
import bz2
s = b'witch which has which witches wrist watch'
with bz2.open('test.bz2', 'wb') as f:
    f.write(s)
with bz2.open('test.bz2', 'rb') as f:
    print(f.read())

# 使用zip压缩
import zipfile
with zipfile.ZipFile('test.zip', 'w') as f:
    f.write('test.txt')
with zipfile.ZipFile('test.zip', 'r') as f:
    print(f.printdir())
   
