from lzma import LZMADecompressor
LZMADecompressor()

def unzlib(zipData):
    return zlib.decompress(zipData)

def untar(data):
    with tarfile.open(fileobj=BytesIO(data)) as tf:
        return tf.getnames()


