import lzma
# Test LZMADecompressor.read() method

def write_read_decompressor(data, chunksize=1):
    compressor = lzma.LZMACompressor()
    compressed = compressor.compress(data)
    compressed += compressor.flush()
    #print(len(compressed))
    decompressor = lzma.LZMADecompressor()
    dec = b''
    for i in range(0, len(compressed), chunksize):
        dec += decompressor.decompress(compressed[i:i+chunksize])
    dec += decompressor.flush()
    return dec

