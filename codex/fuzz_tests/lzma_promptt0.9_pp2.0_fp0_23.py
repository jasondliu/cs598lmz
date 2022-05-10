import lzma
# Test LZMADecompressor
# ref: https://docs.python.org/3.4/library/lzma.html
def decompress(data):
    decompressor = lzma.LZMADecompressor()
    chunk = decompressor.decompress(data)
    if decompressor.unused_data:
        raise ValueError("There are unused_data")
    if decompressor.eof:
        raise ValueError("End of file reached")
    # try:
    #     decompressor.flush()
    # except IOError:
    #     pass
    return chunk
# Test LZMADecompressor
# ref: https://docs.python.org/3.4/library/lzma.html
def decompress(data):
    decompressor = lzma.LZMADecompressor()
    return decompressor.decompress(data)
def list_all_h5_files(path):
    to_return = []
    if os.path.isdir(path):
        candidates = os.listdir(path)
        candidates = [os.path.join(
