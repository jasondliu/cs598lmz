import lzma
# Test LZMADecompressor

def decompress_file(fname):
    r = open(fname, 'rb')
    d = lzma.LZMADecompressor()
    data = d.decompress(r.read())
    r.close()
    print("Length of decompressed data:", len(data))
    return data

def decompress_file_nicely(fname):
    r = open(fname, 'rb')
    d = lzma.LZMADecompressor()
    data = d.decompress(r.read())
    r.close()
    w = open("payload.decompressed", 'wb')
    w.write(data)
    w.close()

decompress_file_nicely("payload.lzma")

(decompress_file("payload.decompressed") == decompress_file("payload"))

(decompress_file("payload.decompressed") == decompress_file("payload.lzma"))

crc32("payload")
crc32("
