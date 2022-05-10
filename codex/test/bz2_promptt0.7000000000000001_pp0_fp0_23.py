import bz2
# Test BZ2Decompressor
# with open("../data/shakespeare.txt.bz2", 'rb') as src, open("../data/shakespeare.txt", 'w') as tgt:
#     decompressor = bz2.BZ2Decompressor()
#     for block in iter(lambda: src.read(1024 * 1024), b''):
#         tgt.write(decompressor.decompress(block).decode("utf-8"))
#     tgt.write(decompressor.flush().decode("utf-8"))
# Test BZ2Compressor
