import bz2
bz2.BZ2File('/tmp/test.bz2', 'w').write(data)
bz2.BZ2File('/tmp/test.bz2', 'r').read()

# compress to bz2
import gzip
gzip.open('/tmp/test.gz', 'w').write(data)
gzip.open('/tmp/test.gz', 'r').read()

# compress to gzip
import lzma
lzma.LZMAFile('/tmp/test.xz', 'w').write(data)
lzma.LZMAFile('/tmp/test.xz', 'r').read()

# compress to xz
import zipfile
zipfile.ZipFile('/tmp/test.zip', 'w').write('/tmp/test.txt')
zipfile.ZipFile('/tmp/test.zip', 'r').read('test.txt')

# compress to zip
import tarfile
tarfile.open('/tmp/test.tar', 'w').write('/tmp/test.txt')
tarfile.
