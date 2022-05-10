import bz2
bz2.decompress(file)
</code>
However, I get an error:
<code>Traceback (most recent call last):
  File "&lt;pyshell#9&gt;", line 1, in &lt;module&gt;
    bz2.decompress(file)
  File "C:\Python31\lib\bz2.py", line 234, in decompress
    return BZ2Decompressor().decompress(data)
  File "C:\Python31\lib\bz2.py", line 217, in decompress
    raise ValueError("invalid data stream")
ValueError: invalid data stream
</code>
I'm not exactly sure what is wrong here.


A:

You need to read from <code>file</code> first:
<code>file.seek(0)
data = file.read()
</code>
<code>file</code> is an empty file object, there is no data to decompress.

