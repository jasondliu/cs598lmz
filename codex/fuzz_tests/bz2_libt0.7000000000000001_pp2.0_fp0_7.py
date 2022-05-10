import bz2
bz2.decompress(bz2.compress(b"A" * 10))
# b'AAAAAAAAAA'

bz2.decompress(bz2.compress(b"A" * 100))
# b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
</code>
lzma:
<code>import lzma
lzma.decompress(lzma.compress(b"A" * 10))
# b'AAAAAAAAAA'

lzma.decompress(lzma.compress(b"A" * 100))
# b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
</code>
As you can see, the output for both is the same. 

