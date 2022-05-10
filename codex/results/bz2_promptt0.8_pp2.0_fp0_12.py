import bz2
# Test BZ2Decompressor without reading the entire stream.

class BZ2TestDecompressor(bz2.BZ2Decompressor):

    def decompress(self, data):
        print(data)
        #super().decompress(data)
        #assert False, 'Should not get here.'
        return super().decompress(data)

compressor = bz2.BZ2Compressor()
firstString = "I went to see my friend the other day, and found him ill in bed."

decompressed = compressor.compress(firstString) + compressor.flush()
print("decompressed: %r" % (decompressed))

#decompressor = BZ2TestDecompressor()
decompressor = bz2.BZ2Decompressor()
decompressed = decompressor.decompress(decompressed + b'invalid data')
print("output: %r" % (decompressed))
print("unused_data: %r" % (decompressor.unused_data))

decompressed = decompressor.decompress(decompressor.
