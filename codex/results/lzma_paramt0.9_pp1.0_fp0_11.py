from lzma import LZMADecompressor
LZMADecompressor().decompress

from lz4.frame import compressed
compressed
</code>
Outputs the following
<code>&lt;class 'lzma.LZMACompressor'&gt;
&lt;class 'lzma.LZMADecompressor'&gt;
&lt;function compressed at 0x7f6e5f5a5d08&gt;
</code>
Now trying to install the C extension version of lz4
<code>pip3 install lz4
</code>
=> Outputs that the package is already satisfied
<code>Requirement already satisfied: lz4 in /usr/local/lib/python3.7/site-packages (3.1.0)
Requirement already satisfied: cffi&gt;=1.0 in /opt/local/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (from lz4) (1.12.2)
Requirement already satisfied: pycparser in /usr/local/lib/python3.7/site-packages (from c
