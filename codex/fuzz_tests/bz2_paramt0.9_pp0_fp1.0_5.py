from bz2 import BZ2Decompressor
BZ2Decompressor
</code>
then the <code>ValueError</code> is raised. Here is the trace back:
<code>Traceback (most recent call last):
File "&lt;stdin&gt;", line 1, in &lt;module&gt;
File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/bz2.py", line 122, in &lt;module&gt;
from _bz2 import BZ2Compressor, BZ2Decompressor
ValueError: Attempted relative import in non-package
</code>
any suggestions?


A:

It seems that bz2 tries to import the <code>_bz2</code> module. You may try to install bz2 from macports. Then you should be able to use python/bz2 from macports if you specify this path as search path for your python interpreter.

