import bz2
bz2.open('/tmp/example.bz2').read()

# gzip
# import gzip
# gzip.open('/tmp/example.gzip').read()

# lzma
# import lzma
# lzma.open('/tmp/example.xz').read()

# zip
import zipfile
zipfile.ZipFile('/tmp/example.zip').read('README.txt')

# tar
import tarfile
tarfile.open('/tmp/example.tar.gz').read()

# cpio
# import cpio
# cpio.open('/tmp/example.cpio').read()

# ar
# import ar
# ar.open('/tmp/example.ar').read()

# rpm
# import rpm
# rpm.open('/tmp/example.rpm').read()

# pax
# import pax
# pax.open('/tmp/example.pax').read()

# dpkg
# import dpkg
# dpkg.open('/tmp/example.deb').read()

# git
