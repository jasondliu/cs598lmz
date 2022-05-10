import lzma
lzma.LZMA_FILTER_ARM

def lzma_compress(data):
    return lzma.compress(data, preset=9 | lzma.PRESET_EXTREME)

def lzma_decompress(data):
    return lzma.decompress(data)

def lzma_decompress_file(filename):
    with lzma.open(filename) as f:
        return f.read()

def lzma_compress_file(data, filename):
    with lzma.open(filename, "w") as f:
        f.write(data)

def lzma_compress_file_from_file(in_filename, out_filename):
    with open(in_filename, "rb") as f_in:
        data = f_in.read()
    lzma_compress_file(data, out_filename)

def lzma_decompress_file_to_file(in_filename, out_filename):
    data = lzma_decomp
