import bz2
# Test BZ2Decompressor and BZ2Compressor.

comp = bz2.BZ2Compressor()

if bytes is not str:
    input = input.encode()
compressed = comp.compress(input) + comp.flush()

decomp = bz2.BZ2Decompressor()
decompressed = decomp.decompress(compressed)

assert decompressed == input, "input != decompressed (%r)" % decompressed
# Test block oriented compress/decompress.

comp = bz2.BZ2Compressor()

assert blocks[0] == "BZh91AY&SY"
out_blocks = [comp.compress(block) for block in blocks]
out_blocks.append(comp.flush())

decomp = bz2.BZ2Decompressor()
decompressed_blocks = []
for block in out_blocks:
    decompressed_blocks.append(decomp.decompress(block))

decompressed = b"".join(decompressed_blocks)

assert decompressed == input, "input != decompressed (%r
