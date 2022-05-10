from lzma import LZMADecompressor
LZMADecompressor()

def unzlib(zipData):
    return zlib.decompress(zipData)

def untar(data):
    with tarfile.open(fileobj=BytesIO(data)) as tf:
        return tf.getnames()


for f in files:
    try:
        tiffs = []
        tarfiles = tarfile.open(f, mode='r|')
        for entry in tarfiles:
            if entry.name.endswith(".tif"):
                tiffs.append(entry.name)

            else:
                f = tarfiles.extractfile(entry)
                f.read()

    finally:
        tarfiles.close()
    print(tiffs)
</code>


A:

try this:
<code>import gzip
import codecs</code>
<code>gzfile_obj = gzip.open('test1.gz', 'rb') # the 2nd arg, 'rb' read bytes instead of strings</code>
<code>first_line = gzfile_obj.readline()
</code>

