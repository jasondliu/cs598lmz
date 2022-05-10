import lzma
lzma.LZMAFile(filename)
</code>
But I get the following error:
<code>Traceback (most recent call last):
  File "C:\Users\user\Desktop\lzma.py", line 2, in &lt;module&gt;
    lzma.LZMAFile(filename)
  File "C:\Python32\lib\lzma.py", line 60, in __init__
    self.fileno = _file_unbuffered.fileno
AttributeError: 'function' object has no attribute 'fileno'
</code>
What should I do?


A:

As stated in the comments, you need to pass a file object to <code>lzma.LZMAFile</code>:
<code>import lzma
with open(filename, 'rb') as f:
    lzma.LZMAFile(f)
</code>
I recommend you to use the <code>with</code> statement, which ensures that the file is closed at the end of the block.

