import lzma
lzma.decompress(compressed_wiki)
try:
    lzma.decompress(compressed_wiki + b'0')
except:
    print('error')
 
# -------------------Taken from stackoverflow-----------
def crc32(data):
    return (binascii.crc32(data) & 0xFFFFFFFF)

def LZMADecompress(compressedData):
    decompress = lzma.LZMADecompressor()
    data = decompress.decompress(compressedData)
    if decompress.eof:
        return data
    else:
        raise MalformedDataError("Compressed data ended before the end-of-stream marker was reached")

def LZMACompress(data, preset=9 | lzma.PRESET_EXTREME):
    compress = lzma.LZMACompressor(format=lzma.FORMAT_RAW, check=-1, preset=preset)
    compressedData = compress.compress(data)
    compressedData += compress.flush()
    return
