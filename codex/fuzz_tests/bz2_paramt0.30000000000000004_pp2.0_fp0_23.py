from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(b'hello world!'))

# bz2.open()
# bz2.open() is a shortcut for creating a BZ2File object, calling its read() or write() method, and closing the file.
# It accepts the same arguments as BZ2File.

# bz2.compress()
# bz2.compress() accepts a single argument, which can be either a bytes object or a file object. If the argument is a bytes object, it returns a compressed version of that bytes object; if it’s a file object, it compresses the data read from the file object and returns the compressed data as a bytes object.
# bz2.decompress()
# bz2.decompress() accepts a single argument, which can be either a bytes object or a file object. If the argument is a bytes object, it returns a decompressed version of that bytes object; if it’s a file object, it decompresses the data read from the file object and returns the decompressed data as a bytes object.

# Example
# The following example shows how to compress
