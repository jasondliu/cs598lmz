from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(payload_ID)
</code>
gives me an error:
<code>    Traceback (most recent call last):   File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: BZ2Decompressor.decompress() argument 1 must be string without null bytes, not str
</code>
I have tried to convert the string to bytes using encode and that doesn't work either. I know the issue is related to the string having null bytes in it, but how do I get rid of those null bytes?


A:

A <code>\x00</code> byte is a null byte. If you want to remove all null bytes from a string, use:
<code>payload_ID = payload_ID.replace('\x00', '')
</code>
as you don't want to treat the string as a byte string, you don't need to encode it first.

