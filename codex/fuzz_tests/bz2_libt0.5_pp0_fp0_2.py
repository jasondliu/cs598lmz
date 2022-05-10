import bz2
bz2.BZ2File('sample.bz2')

# gzip
import gzip
gzip.open('sample.gz')

# lzma
import lzma
lzma.open('sample.xz')

# tarfile
import tarfile
tar = tarfile.open('sample.tar.gz')
tar.getmembers()
tar.extractall()
tar.close()

# zipfile
import zipfile
zip = zipfile.ZipFile('sample.zip')
zip.getinfo('sample.txt')
zip.extract('sample.txt')
zip.close()

# struct
import struct
struct.pack('>I', 10240099)
struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')

# hashlib
import hashlib
hashlib.md5(b'how to use md5 in python hashlib?').hexdigest()
hashlib.sha1(b'how to use sha1 in python hashlib?').hexdigest()

# hmac
