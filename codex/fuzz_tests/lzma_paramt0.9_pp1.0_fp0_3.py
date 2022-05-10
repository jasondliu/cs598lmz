from lzma import LZMADecompressor
LZMADecompressor().decompress(x)

</code>
and the error is : 
<blockquote>
<p>error: Error -3 while decompressing data: invalid distance too far back
  Exception ignored in: &gt;
  Traceback (most recent call last):   File
  "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/lzma.py",
  line 375, in <strong>del</strong>
      self.close()   File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/lzma.py",
  line 384, in close
      self.decompress(EOF_MARKER, eof=True)   File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/lzma.py",
  line 373, in decompress
      data = ffi.buffer(data_ptr, used_out[0])[:] TypeError: memoryview: a bytes-like object is required, not
