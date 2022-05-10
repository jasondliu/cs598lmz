import lzma
lzma_path = "./"
lzma_lib = lzma.LZMAFile("%s/libxz.a" % lzma_path, "r")
lzma_lib_content = lzma_lib.read()
lzma_lib.close()

def uncompress_lzma(data):
    output = StringIO()
    output.write(data)
    output.seek(0)
    lzma_decoder = lzma.LZMADecompressor()
    return lzma_decoder.decompress(output.read())

def compress_lzma(data):
    output = StringIO()
    lzma_compressor = lzma.LZMACompressor()
    lzma_compressor.compress(data)
    lzma_compressor.flush(output)
    return output.getvalue()

# Main part of the script
if len(sys.argv) < 4:
    print "Usage: %s input.lzma output.lzma compression_level
