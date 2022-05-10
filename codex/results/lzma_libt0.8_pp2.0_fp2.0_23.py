import lzma
lzma.decompress(lzma.compress(b'Hello'))

# another example from gzip import GzipFile
from io import BytesIO
import gzip
s = BytesIO()
gf = gzip.GzipFile(fileobj=s, mode='wb')
gf.write(b'Hello\n')
gf.close()
print(s.getvalue())

s2 = BytesIO(s.getvalue())
gf2 = gzip.GzipFile(fileobj=s2)
print(gf2.read())

#zipfile
import zipfile

with zipfile.ZipFile('test.zip', 'w') as zf:
    zf.write('test.py')

with zipfile.ZipFile('test.zip', 'r') as zf:
    print(zf.namelist())
    print(zf.getinfo('test.py'))

#tar
import tarfile
with tarfile.open('test.tar', 'w') as tf:
    tf.add('test.py')
