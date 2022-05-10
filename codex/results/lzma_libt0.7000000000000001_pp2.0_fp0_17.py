import lzma
lzma.decompress((open("data1.txt.xz", "rb")).read())

# b'The quick brown fox jumps over the lazy dog.'

(open("data1.txt", "wb")).write(lzma.decompress((open("data1.txt.xz", "rb")).read()))
</code>

