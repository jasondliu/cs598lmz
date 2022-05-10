from bz2 import BZ2Decompressor
BZ2Decompressor.decompress(f_in.read(size))
</code>
To read from standard input:
<code>from bz2 import decompress
decompress(sys.stdin.read())
</code>

