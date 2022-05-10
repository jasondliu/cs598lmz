from lzma import LZMADecompressor
LZMADecompressor()
```

```
$ python test.py
/usr/lib64/python2.7/site-packages/lzmaffi/lzma.py:53: RuntimeWarning: Could not find liblzma. LZMA compression is not available.
  warnings.warn("Could not find liblzma. LZMA compression is not available.", RuntimeWarning)
Traceback (most recent call last):
  File "test.py", line 7, in <module>
    LZMADecompressor()
  File "/usr/lib64/python2.7/site-packages/lzma/errors.py", line 35, in __init__
    super(LZMADecompressor, self).__init__(format=FORMAT_XZ,
  File "/usr/lib64/python2.7/site-packages/lzma/lzma.py", line 69, in __init__
    self._decompressor = _lzma.LZMADecompressor()
ValueError: failed to initialize _lzma.LZMADecomp
