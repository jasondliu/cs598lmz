import lzma
lzma.decompress(lzma.compress(b'hello'))

# 2.7.8 ----------------------------------
#import bz2
#bz2.decompress(bz2.compress(b'hello'))

# 2.7.10 ---------------------------------
#import zlib
#zlib.decompress(zlib.compress(b'hello'))

# 2.7.11 ---------------------------------
#import zipfile, tarfile
#with zipfile.ZipFile('myfile.zip') as zf:
#    zf.extractall()
#with tarfile.TarFile('myfile.tar') as tf:
#    tf.extractall()

# 2.7.12 ---------------------------------
#import subprocess
#subprocess.Popen(['c:\Program Files\Internet Explorer\IEXPLORE.EXE'])
