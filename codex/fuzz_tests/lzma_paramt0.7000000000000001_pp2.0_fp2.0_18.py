from lzma import LZMADecompressor
LZMADecompressor.__init__()
</code>
The last line above throws an exception:
<code>TypeError: descriptor '__init__' requires a 'lzma.LZMADecompressor' object 
but received a 'int'
</code>
I have tried using both the <code>lzma</code> and <code>pyliblzma</code> modules.
I am using Python 3.2.2 on Windows 7 64-bit.
Does anyone know how to use <code>lzma</code> to decompress a simple stream?
EDIT:
I am seeing the same problem in Linux, so it is not a Windows specific problem.


A:

<code>LZMADecompressor.__init__()</code> is not correct.  You need to create an instance of the object before you can call <code>decompress()</code>:
<code>import lzma
decomp = lzma.LZMADecompressor()
decomp.decompress(input)
</code>

