import lzma
# Test LZMADecompressor by decompressing the first 1024 bytes.
decompressobj = lzma.LZMADecompressor()
decompressed = decompressobj.decompress(testdata, 1024)
</code>
But I'm getting an error.
<code>Traceback (most recent call last):
  File "testfile.py", line 6, in &lt;module&gt;
      decompressed = decompressobj.decompress(testdata, 1024)
  File "lzma.pyx", line 864, in lzma.LZMADecompressor.decompress (src/lzma.c:8383)
  File "lzma.pyx", line 812, in lzma.LZMADecompressor.decompress (src/lzma.c:7932)
  File "lzma.pyx", line 256, in lzma.check_size (src/lzma.c:6938)
lzma.LZMAError: Input format not supported by decoder
</code>
I'm not sure why it's
