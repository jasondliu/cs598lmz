from lzma import LZMADecompressor
LZMADecompressorObj = LZMADecompressor()

ofn = 'va_full.xcf'
with open(ofn, 'wb') as ofd:
    ofd.write(LZMADecompressorObj.decompress(va_full_xcf_lzma))
