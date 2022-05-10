from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(f)
</code>
<blockquote>
<p>Traceback (most recent call last):   File "", line 1, in
     File
  "/usr/local/Cellar/python/3.7.3/Frameworks/Python.framework/Versions/3.7/lib/python3.7/bz2.py",
  line 71, in decompress
      raise ValueError("incomplete start byte") ValueError: incomplete start byte</p>
</blockquote>
Any ideas?
Also is it possible to read the file directly from the GCS bucket via HTTP?

