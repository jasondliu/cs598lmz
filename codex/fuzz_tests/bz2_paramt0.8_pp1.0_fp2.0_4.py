from bz2 import BZ2Decompressor
BZ2Decompressor(open('comp.bz2', 'rb')).decompress()


# bzip2 file
# import subprocess
# subprocess.call(["bzip2", "-c", "file"])
# subprocess.call(["bzip2", "-d", "file.bz2"])


# uncompress gzip file
import gzip
gzip.open('file.gz', 'rb').read()

# compress gzip file
import gzip
f_in = open('file', 'rb')
f_out = gzip.open('file.gz', 'wb')
f_out.writelines(f_in)
f_out.close()
f_in.close()

# zlib compress
import zlib
zlib.compress('string to compress')
zlib.decompress(b'x\x9c\xcbH\xcd\xc9\xc9W(\xcf/\xcaI\x01\x00+\x80\x03\x00\x04\x00\x05\x00\x06\x00
