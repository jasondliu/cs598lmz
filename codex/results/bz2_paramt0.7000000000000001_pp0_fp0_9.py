from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed_data)
</code>
But it doesn't work as expected.
I don't know what <code>BZ2Decompressor</code> actually does, but I assume that it's some kind of stream object and it decompresses the data it receives. So far, so good.
But how can I feed it my data?
I tried passing it a <code>BytesIO</code> instance, but that didn't work either.


A:

The documentation for <code>BZ2Decompressor</code> says it expects a <code>bytearray</code> as input and returns a <code>bytearray</code> as output.  You can use the <code>io.BytesIO</code> class to wrap your input data:
<code>import io
import bz2

input = io.BytesIO(compressed_data)
decompressor = bz2.BZ2Decompressor()
output = io.BytesIO()

while True:
    block = input.read(100)
    if block == b'':
        break
    output
