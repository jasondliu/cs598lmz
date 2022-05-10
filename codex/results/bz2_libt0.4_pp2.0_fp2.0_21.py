import bz2
bz2_file = bz2.BZ2File('data/file.bz2')
data = bz2_file.read()
bz2_file.close()

# gzip
import gzip
gz_file = gzip.open('data/file.gz', 'rt')
data = gz_file.read()
gz_file.close()

# lzma
import lzma
lzma_file = lzma.open('data/file.xz')
data = lzma_file.read()
lzma_file.close()

# tar
import tarfile
tar = tarfile.open('data/file.tar.gz')
for member_info in tar.getmembers():
    print(member_info.name)
    print(member_info.size)
    tar.extract(member_info, path='data/tar_extract')
tar.close()
