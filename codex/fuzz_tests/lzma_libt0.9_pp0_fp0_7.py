import lzma
lzma.decompress(data[0])
</code>
Here's the stderr part of the traceback:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/home/alex/lib/python2.7/site-packages/paramiko/py3compat.py", line 86, in execfile
    exec(compiler(f.read(), fname, 'exec'), glob, loc)
  File "&lt;stdin&gt;", line 3, in &lt;module&gt;
  File "/usr/lib/python2.7/lzma.py", line 286, in decompress
    return _decompress(decompressor, data, format)
TypeError: must be string or buffer, not tuple
</code>
So I'm not sure if this is paramiko or just lzma but either way, I'm not using a tuple and shouldn't be getting this error.  At the same time, I'm not sure what to do to fix it.



