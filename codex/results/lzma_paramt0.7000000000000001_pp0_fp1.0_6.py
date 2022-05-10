from lzma import LZMADecompressor
LZMADecompressor().decompress(data)
</code>
And I get the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
  File "lzma.pyx", line 656, in lzma.LZMADecompressor.decompress (src/lzma.c:10698)
lzma.LZMAError: Input format not supported by decoder
</code>
I tried to use the <code>format</code> parameter of <code>LZMADecompressor</code>, but in the documentation it says that it is deprecated.
How can I decompress the data?


A:

<code>lzma</code> is a low-level API; the <code>format</code> parameter was used to select the LZMA bitstream format. This parameter is deprecated because the input data format is automatically detected.
The <code>lzma</code> module does not support the XZ file format. You need to use <code>xzfile</
