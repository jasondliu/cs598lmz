from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# this doesn't work because the compression is streamed
# decompress(data)

# THIS DOES WORK
# decompress(data[0:-4])
</code>
I'm not sure what the last 4 bytes are. 
So, the question is:
How can I use Python's bz2 module to decompress a bz2 file that has been uploaded via a form?


A:

You need to use <code>BytesIO</code> to make a file-like object out of the bytes you have received. <code>bz2.BZ2Decompressor</code> can then read from that object:
<code>import bz2
from io import BytesIO

# Make a BytesIO object
compressed_data = BytesIO(data)

# Create a decompressor object
decompressor = bz2.BZ2Decompressor()

# Decompress the data and print it
decompressed_data = decompressor.decompress(compressed_data.read())
print(decompressed_data)
</code>

