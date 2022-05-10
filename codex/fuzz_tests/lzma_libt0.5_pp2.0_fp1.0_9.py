import lzma
lzma.open(file_name)
</code>
The following is the error message:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/opt/local/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lzma.py", line 21, in open
    return LZMAFile(filename, mode, **kwargs)
  File "/opt/local/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lzma.py", line 75, in __init__
    self._lzma = _lzma.LZMAFile(filename, mode, **kwargs)
AttributeError: module '_lzma' has no attribute 'LZMAFile'
</code>


A:

If you look at the code for <code>lzma.py</code> in Python 3.6, you'll see that it attempts to import <code>_lzma</code> as a
