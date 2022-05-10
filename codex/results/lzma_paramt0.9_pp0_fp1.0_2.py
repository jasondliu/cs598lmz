from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

b'hello world!hello world!hello world!hello world!hello world!hello world!'

b'hello world!hello world!hello world!hello world!hello world!hello world!'

In [3]: 

from lzma import LZMACompressor
compressor = LZMACompressor()
bytestream = b''
for i in range(5):
    chunk = compressor.compress(b'hello world!')
    bytestream += chunk
bytestream += compressor.flush()
LZMADecompressor().decompress(bytestream)

b'hello world!hello world!hello world!hello world!hello world!'

b'hello world!hello world!hello world!hello world!hello world!'
</code>
But this give me an error
<code>f = lzma.open(file, mode='ab')
 f.write(bytearray)
File "/home/mattia/venvs/personal_projects/lib/python3.6/site-packages/lzma.py", line 29,
