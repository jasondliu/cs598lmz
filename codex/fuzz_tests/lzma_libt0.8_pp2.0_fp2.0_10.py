import lzma
lzma.LZMACompressor.compress(data)
</code>
But I keep getting an error saying:
<code>Traceback (most recent call last):
  File "test.py", line 34, in &lt;module&gt;
    print(lzma.LZMACompressor.compress(data))
  File "/usr/lib/python3.5/lzma.py", line 277, in compress
    raise TypeError("data must be a bytes-like object, not %.200r" % data)
TypeError: data must be a bytes-like object, not &lt;_io.BufferedReader name='1.hdr'&gt;
</code>
I'm not sure what to do to fix this code. 


A:

As the error message says, the <code>compress()</code> function expects a bytes-like object, not a <code>BufferedReader</code> object.
Read the file into a buffer before passing it to the <code>compress()</code> function:
<code>data = file_in.read()

