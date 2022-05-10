import bz2
bz2.BZ2Compressor()

# make sure we can read bz2 files too
import bz2
bz2.BZ2Decompressor()

# make sure we can read tar files too
import tarfile
tarfile.open()

# make sure we can read tar.gz files too
import tarfile
tarfile.open()
</code>
I get an error:
<code>&gt;&gt;&gt; import bz2
&gt;&gt;&gt; bz2.BZ2Compressor()
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/local/python-2.7.6/lib/python2.7/bz2.py", line 27, in &lt;module&gt;
    from _bz2 import BZ2Compressor, BZ2Decompressor
ImportError: No module named _bz2
&gt;&gt;&gt; import bz2
Traceback (most recent call
