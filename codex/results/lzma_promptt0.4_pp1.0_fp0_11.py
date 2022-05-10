import lzma
# Test LZMADecompressor with a file that is not compressed with XZ.
with open("/etc/hosts", "rb") as f:
    with lzma.LZMADecompressor() as decompressor:
        decompressor.decompress(f.read())
# Traceback (most recent call last):
#   File "<stdin>", line 3, in <module>
#   File "/usr/lib/python3.7/lzma.py", line 527, in decompress
#     return self.decompressobj.decompress(data, max_length)
#   File "/usr/lib/python3.7/lzma.py", line 459, in decompress
#     raise LZMAError("Input format not recognized")
# lzma.LZMAError: Input format not recognized

# Test LZMADecompressor with a file that is compressed with XZ.
with open("/etc/hosts.xz", "rb") as f:
    with lzma.LZMADecompressor() as decompressor:
        decompressor.decompress
