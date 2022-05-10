import bz2
# Test BZ2Decompressor
compressed_file = bz2.BZ2File("enwik8_compressed.bz2", "wb")
compressed_file.write(open("enwik8", "rb").read())
compressed_file.close()


# BZ2Compressor is a stateful transform: it accumulates input data into an internal buffer until it is flushed.
# Because of this, it’s necessary to call its close() method when data has been processed.
compressor = bz2.BZ2Compressor()

with open("enwik8_compressed.bz2", "wb") as compressed_file:
    with open("enwik8", "rb") as original_file:
        while True:
            block = original_file.read(100000)
            if not block:
                break
            compressed_file.write(compressor.compress(block))
        compressed_file.write(compressor.flush())

decompressor = bz2.BZ2Decompressor()
with open("enwik8_compressed.bz2", "rb") as compressed_
