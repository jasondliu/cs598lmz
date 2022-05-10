import bz2
# Test BZ2Decompressor with data that contains:
#   - multiple small compressed blocks,
#   - multiple small uncompressed blocks

def getSmallBlocksOfData(iterations):
    table = ''.join(chr(c) for c in xrange(256)) * 16 + 'hello' * 16
    for i in xrange(iterations):
        nblocks, blocklen = random.randrange(1,10), random.randrange(1,100)
        compressed = ''.join(random.choice(table) for _ in xrange(nblocks * blocklen))
        yield (bz2.compress(compressed), compressed)

# Test decompress with varying length input buffers
for inbuffer_len in range(1,20):
    decomp = bz2.BZ2Decompressor()
