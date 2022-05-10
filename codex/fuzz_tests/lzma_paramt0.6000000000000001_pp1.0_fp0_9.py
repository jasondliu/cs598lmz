from lzma import LZMADecompressor
LZMADecompressor()
</code>
This fails with the error message:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "/usr/lib/python3.4/lzma.py", line 29, in __init__
    super(LZMADecompressor, self).__init__(format=FORMAT_RAW, check=-1,
AttributeError: module 'lzma' has no attribute 'FORMAT_RAW'
</code>
I don't understand why this is happening. It seems like the same version of Python should have the same version of the module, and if anything I would expect the system-wide version to be older than the one in the virtual environment.
I'm running Python 3.4.3 on Ubuntu 15.04.
Update:
I checked the version of the lzma module in the virtual environment, and it is indeed newer than the one on the system:
<code>$ python3 -c 'import lzma; print(lzma.__version__)'
5.2.2

