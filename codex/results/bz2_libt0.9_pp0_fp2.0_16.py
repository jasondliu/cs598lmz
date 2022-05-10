import bz2
bz2file=bz2.BZ2File("sample..bz2")
type(bz2file)

data=bz2file.read()
type(data)

data.decode("utf-8")
len(data)

data[:50]

#gzip
import gzip
gzfile=gzip.GzipFile("sample.gzip", "rb")
d=gzfile.read()
len(d)
d[:50]
d.decode("utf-8")

import zlib
z=zlib.compress(b"Hello World")
z
z.decode("utf-8")
len(z)
zlib.decompress(z)
zlib.decompress(z).decode("utf-8")
len(zlib.decompress(z))
z=zlib.compress(b"Hello World!")
zlib.decompress(z)
zlib.decompress(z, 15)
zlib.decompress(z, 16)
z2=zlib.compress(
