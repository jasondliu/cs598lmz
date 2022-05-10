import lzma
# Test LZMADecompressor
decompressor = lzma.LZMADecompressor()
chunks = []
while True:
    chunk = file.read(4 * 1024)
    if len(chunk) == 0:
        break
    chunks.append(decompressor.decompress(chunk))

data = b''.join(chunks)
</code>
But, I get the following error:
<code>Traceback (most recent call last):
  File "/home/lucas/Documents/github/python-lzma/test.py", line 15, in &lt;module&gt;
    chunks.append(decompressor.decompress(chunk))
  File "/usr/lib/python3.6/lzma.py", line 790, in decompress
    return self.decompressobj.decompress(data, max_length)
  File "/usr/lib/python3.6/lzma.py", line 595, in decompress
    self._buffer = self._buffer[consumed:] + input
TypeError: can only concatenate str (
