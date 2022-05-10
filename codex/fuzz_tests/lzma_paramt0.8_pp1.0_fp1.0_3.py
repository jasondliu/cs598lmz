from lzma import LZMADecompressor
LZMADecompressor().decompress(chunk)

from bz2 import decompress
decompress(chunk)
</code>
But neither of them work. The output is not readable. I have also tried using <code>xz</code> and <code>lz4</code> with the same results.
I am using python 3.5.


A:

You can try using the <code>unxz</code> command. You can read the data from the command output and process it. Here is the command.
<code>unxz myDataFile.xz</code>
And then read the uncompressed data from the command output.
This is done in Python 3.7.

