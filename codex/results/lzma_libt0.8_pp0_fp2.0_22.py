import lzma
lzma.open(infile)
</code>
It tells:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
IOError: [Errno 2] No such file or directory: 'B.15.8.23.txt.xz'
</code>
I tried to find the module by:
<code>$ tar -tvf python.tar | grep xz
drwxr-xr-x root/root         0 2010-12-30 20:46 python/Modules/_lzma/
-rw-r--r-- root/root      3276 2010-12-30 20:46 python/Modules/_lzma/__init__.py
-rw-r--r-- root/root     56154 2010-12-30 20:46 python/Modules/_lzma/delta.h
-rw-r--r-- root/root     29061 2010-12-30 20:46 python/Modules/_lzma/lzma.h
-rw-r
