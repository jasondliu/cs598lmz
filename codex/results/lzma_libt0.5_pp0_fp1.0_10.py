import lzma
lzma.decompress(test)
</code>
I am trying to decompress a <code>bytes</code> object, but this gives me the error:
<code>TypeError: a bytes-like object is required, not 'str'
</code>
I am not sure how to go about decompressing this.


A:

The <code>bytes</code> object you get from <code>base64.b64decode</code> is not a valid lzma stream. It contains a header, a footer, and some other stuff that is not part of the lzma stream.
The header is a 32-bit unsigned integer, which is the size of the uncompressed data. The footer is a 32-bit CRC32 checksum of the uncompressed data.
You can use the <code>lzma.open</code> function to decompress the data, but you need to give it the correct size and CRC. You can find the size in the header, and the CRC in the footer.
<code>import lzma
import base64
import struct

data = base64.b64decode(test
