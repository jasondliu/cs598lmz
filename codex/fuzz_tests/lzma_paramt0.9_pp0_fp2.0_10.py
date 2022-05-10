from lzma import LZMADecompressor
LZMADecompressor.decompress(data)

Output:
mydata
d=b"mydata"
import lzma
from io import BytesIO
compressor =  lzma.LZMACompressor()
buf=BytesIO()
buf.write(compressor.compress(d))
buf.seek(0)
print(buf.read())
print(compressor.flush())
buf.write(compressor.compress(d))
buf.write(compressor.flush())
buf.seek(0)
d=buf.read()

lzma.LZMADecompressor().decompress(d)

Output:
b'\x00\x04\x00\x04\x00\x04\x03\x01\r\x00\x01\x00\xff\xff\xff'
b'\x00\x02\x00\x00\x01\x00\x00\x04\x06\xb8\x10\x00\x00\x00\x00\x10\x00\x00\x00
