import lzma
lzma_comp = lzma.LZMACompressor(format=lzma.FORMAT_RAW, filters=[{"id" : lzma.FILTER_LZMA1, "dict_size" : lzma.DICT_SIZE_MIN}])

with open(sys.argv[1], "rb") as f:
    fb = f.read(1048576)

    while fb:
        sys.stdout.buffer.write(lzma_comp.compress(fb))
        fb = f.read(1048576)

sys.stdout.buffer.write(lzma_comp.flush())
