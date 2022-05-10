import lzma
lzma.open(file_path)
</code>
I'm getting the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "C:\Python27\lib\lzma.py", line 86, in open
    return LZMAFile(filename, mode, **kwargs)
  File "C:\Python27\lib\lzma.py", line 99, in __init__
    fileobj = _builtin_open(filename, mode)
IOError: [Errno 2] No such file or directory: 'C:\\Users\\me\\Desktop\\test.7z'
</code>
The path is valid and I'm using Python 2.7.10.


A:

I just had the same problem and found the solution in the comments of the lzma.py file:
<blockquote>
<p>The LZMAFile class is a file-like object that reads and writes data
  compressed using the LZMA algorithm.  The class supports reading and
