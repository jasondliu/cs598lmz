from lzma import LZMADecompressor
LZMADecompressor()(data).decode("utf-8")
</code>
The first line is the one that makes the program crash when I run it with PyInstaller.
Here's the error I get:
<code>Traceback (most recent call last):
  File "&lt;string&gt;", line 1, in &lt;module&gt;
  File "&lt;string&gt;", line 5, in try_lzma
  File "lzma.pyx", line 869, in lzma.LZMADecompressor.__init__ (lzma.c:12205)
  File "lzma.pyx", line 645, in lzma.LZMADecompressor.reset (lzma.c:9772)
  File "lzma.pyx", line 930, in lzma.LZMADecompressor.init_filter_properties (lzma.c:15483)
  File "lzma.pyx", line 944, in lzma.LZMADecompressor.set_filter_
