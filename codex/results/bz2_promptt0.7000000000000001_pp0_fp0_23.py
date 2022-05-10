import bz2
# Test BZ2Decompressor
# with open("../data/shakespeare.txt.bz2", 'rb') as src, open("../data/shakespeare.txt", 'w') as tgt:
#     decompressor = bz2.BZ2Decompressor()
#     for block in iter(lambda: src.read(1024 * 1024), b''):
#         tgt.write(decompressor.decompress(block).decode("utf-8"))
#     tgt.write(decompressor.flush().decode("utf-8"))
# Test BZ2Compressor
with open("../data/shakespeare.txt.bz2", 'wb') as tgt:
    compressor = bz2.BZ2Compressor(9)
    with open("../data/shakespeare.txt", 'r') as src:
        for line in src:
            tgt.write(compressor.compress(bytes(line, "utf-8")))
        tgt.write(compressor.flush())
 
with open("../data/shakespeare.txt.bz2", 'rb') as src,
