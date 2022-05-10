from lzma import LZMADecompressor
LZMADecompressor()
</code>
This resulted in a <code>NotImplementedError: LZMA is not supported on this platform</code> error.
I am using Python 3.6 on Windows 10. I have also tried using <code>pylzma</code> but that does not work either.

