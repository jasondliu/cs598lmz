from lzma import LZMADecompressor
LZMADecompressor = LZMADecompressor()

zlib_decompressor = zlib.decompressobj()

def decompress_zlib(s):
    return zlib_decompressor.decompress(s)

def decompress_lzma(s):
    return LZMADecompressor.decompress(s)

def decompress_lzma_lzma(s):
    return LZMADecompressor.decompress(s)

def compress_zlib(s):
    return zlib.compress(s)



def compress_lzma(s):
    return lzma.compress(s)

def compress_lzma_lzma(s):
    return lzma.compress(s)

for f in os.listdir('.'):
    if not f.startswith('google_images_') or not f.endswith('.tar.lzma'):
        continue
    with open(f, 'rb') as fin:
        s = fin.read()
   
