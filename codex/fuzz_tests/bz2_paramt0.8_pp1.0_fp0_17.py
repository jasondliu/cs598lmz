from bz2 import BZ2Decompressor
BZ2Decompressor()
</code>
Each call to <code>BZ2Decompressor</code> fails with the same error.
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "C:\Program Files\Anaconda3\lib\bz2.py", line 360, in __init__
    self.decompress = _create_decompress()
  File "C:\Program Files\Anaconda3\lib\bz2.py", line 358, in _create_decompress
    return _bz2.decompress
AttributeError: 'module' object has no attribute 'decompress'
</code>
Conversely, I can go through a manual install of the bz2file module and everything works just fine.
<code>import bz2file
bz2file.open('some.bz2').read()
</code>
This is the case on two different computers. I've also tried using Anaconda to uninstall and reinstall the module, but no luck.
I
