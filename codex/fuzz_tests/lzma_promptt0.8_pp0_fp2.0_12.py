import lzma
# Test LZMADecompressor with the 'format=FORMAT_ALONE' flag and test
# incompressible input (COMPRESS and COMPRESS_ENCODER_TEST are defined
# in Modules/_lzmamodule.c).
data = b"COMPRESS" + lzma.COMPRESS_ENCODER_TEST

with lzma.open(BytesIO(data), format=lzma.FORMAT_ALONE) as uncomp:
    read_data = uncomp.read()

assert read_data == b"COMPRESS" + lzma.COMPRESS_ENCODER_TEST

class MyCompress0:
    def compress(self, data):
        return data

    def flush(self):
        return b""

class MyCompress1:
    def compress(self, data):
        return data[:1]

    def flush(self):
        return b""

class MyCompress2:
    def compress(self, data):
        return data[:2]

    def flush(self):
        return b""

# Test basic functionality with MyCompress0

