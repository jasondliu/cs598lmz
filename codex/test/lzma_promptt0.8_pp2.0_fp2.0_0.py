import lzma
# Test LZMADecompressor on a file

def decompress(src, dst):
    decompressor = lzma.LZMADecompressor()
    with open(src, 'rb') as input_file, \
        open(dst, 'wb') as output_file:
        for data in iter(lambda: input_file.read(100 * 1024), b''):
            output_file.write(decompressor.decompress(data))
        # LZMA file has end marker, flush to get the last bytes
        output_file.write(decompressor.flush())

def test_lzma(filename):
    print("LZMA")
    in_filename = filename + ".lzma"
    out_filename = filename + ".decoded.lzma"
    print("Compress file with LZMA")
    start = time.time()
    with open('lzma_file.bin', 'rb') as input_file, \
        lzma.open(in_filename, 'wb') as output_file:
        output_file.write(input_file.read())
