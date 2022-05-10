import lzma
lzma.decompress(open('/home/magus/Downloads/xz_files/python-3.7.0.tar.xz', 'rb').read())

# tarfile
import tarfile
tar = tarfile.open('/home/magus/Downloads/python-3.7.0.tar.xz', "r:xz")
tar.extractall(path="/home/magus/Downloads/")
tar.close()

# 压缩
import lzma
lzma.compress(open('/home/magus/Downloads/python-3.7.0/LICENSE', 'rb').read())
lzma.decompress(open('/home/magus/Downloads/python-3.7.0/LICENSE', 'rb').read())

# gzip
import gzip
gzip.compress(open('/home/magus/Downloads/python-3.7.0/LICENSE', 'rb').read())
gzip.decompress(open('/home/magus/Download
