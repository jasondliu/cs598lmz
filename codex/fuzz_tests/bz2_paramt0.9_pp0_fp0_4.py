from bz2 import BZ2Decompressor
BZ2Decompressor.MAX_COPY_SIZE = 102400
f = bz2.open('sample_file.bz2', mode = 'r', compresslevel = 9)
</code>
Above code <code>BZ2Decompressor.MAX_COPY_SIZE = 102400</code> is an example, it depends on your needs.

