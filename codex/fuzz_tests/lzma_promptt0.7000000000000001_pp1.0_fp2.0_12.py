import lzma
# Test LZMADecompressor 
# https://docs.python.org/3/library/lzma.html#lzma.LZMADecompressor

def decompress_lzma(xz_bytes):
    """
    Decompres LZMA file
    """
    lzma_file = lzma.LZMADecompressor()
    lzma_file.format = lzma.FORMAT_AUTO
    dec_txt = lzma_file.decompress(xz_bytes)
    return dec_txt
# Test decompress_lzma

xz_file = '../../data/gns/gns-2018-10-01-00-01-00-L.xz'

dec_txt = decompress_lzma(xz_file)

print(dec_txt)

assert b'\n' in dec_txt

print('OK: decompress_lzma OK')

# Test decompress_lzma

xz_file = '../../data/gns/gns-2018-10-
