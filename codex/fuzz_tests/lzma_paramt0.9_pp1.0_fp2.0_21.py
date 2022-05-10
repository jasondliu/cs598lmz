from lzma import LZMADecompressor
LZMADecompressor().decompress(a.encode('latin_1'))
</code>
But I receive this error:
<code>ValueError: Object size is not a multiple of four
</code>
So, how could I fix this error? Thanks.


A:

Your string <code>a</code> is not in the correct form; it must be encoded in Base64, which is explicitly mentioned in the docs:
<blockquote>
<p>The input must be an XZ-compressed string that has been encoded in
  Base64. If the input is not from a trusted source, it may contain
  malicious data that exploits vulnerabilities in the decoder.</p>
</blockquote>
Therefore to decode, you first need to decode from Base64, and then uncompress:
<code>import base64
from lzma import LZMADecompressor

decompressor = LZMADecompressor()
lzma_object = decompressor.decompress(base64.b64decode(a.encode('latin_1')))
</code>
When you do not encode the <
