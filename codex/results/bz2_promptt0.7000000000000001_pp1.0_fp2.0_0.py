import bz2
# Test BZ2Decompressor
decomp = bz2.BZ2Decompressor()
a = decomp.decompress(b)
len(a)

import bz2

bz2_size = bz2.compress(wiki_text.encode('utf-8')).__sizeof__()
bz2_size

gzip_size = gzip.compress(wiki_text.encode('utf-8')).__sizeof__()
gzip_size

import lzma
lzma_size = lzma.compress(wiki_text.encode('utf-8')).__sizeof__()
lzma_size

zlib_size = zlib.compress(wiki_text.encode('utf-8')).__sizeof__()
zlib_size

print ("bz2 size: {}\ngzip size: {}\nlzma size: {}\nzlib size: {}".format(bz2_size,gzip_size, lzma_size, zlib_size))

# we can see that gzip is the best compression in
