import lzma
lzma.LZMAFile(open("/home/matt/Downloads/foo.xz", "rb"))
</code>
This works fine. But now I want to do the same thing, but with a file-like object instead of a file. I have a file-like object, but when I try to use it with <code>lzma.LZMAFile</code> I get the following error:
<code>&gt;&gt;&gt; lzma.LZMAFile(my_file_like_object)
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python3.4/lzma.py", line 39, in __init__
    self._init_decompressor(fileobj)
  File "/usr/lib/python3.4/lzma.py", line 58, in _init_decompressor
    self._decompressor = lzma.decompressobj()
TypeError: 'module' object is not callable

