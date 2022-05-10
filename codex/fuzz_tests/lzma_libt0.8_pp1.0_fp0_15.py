import lzma
lzma.LZMAError:
Error setting properties: Invalid properties specified for compression.
</code>
thanks for your help.


A:

My mistake is that I use lzma module in python3.x, but the lzma module in python3.x only support compress, not support decompress.

