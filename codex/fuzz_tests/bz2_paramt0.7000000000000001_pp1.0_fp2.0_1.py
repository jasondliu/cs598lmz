from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(
    open("enwik8", "rb").read(10 * 1024 * 1024)
)
</code>
This produces the following traceback:
<code>Traceback (most recent call last):
  File "test.py", line 3, in &lt;module&gt;
    BZ2Decompressor().decompress(open("enwik8", "rb").read(10 * 1024 * 1024))
  File "C:\Program Files (x86)\Python37-32\lib\bz2.py", line 261, in decompress
    return self._buffer.read(size)
  File "C:\Program Files (x86)\Python37-32\lib\bz2.py", line 511, in read
    self._fill(size)
  File "C:\Program Files (x86)\Python37-32\lib\bz2.py", line 571, in _fill
    raise EOFError("Compressed file ended before the "
EOFError: Compressed file ended before the end-of-stream marker was reached
</code>
I am running Python 3
