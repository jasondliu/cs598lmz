import lzma
# Test LZMADecompressor
comp = lzma.LZMADecompressor()
comp

#comp.decompress(b'\xf0\x9f\x8d\xa3')

#comp.decompress(b'\xf0\x9f\x8d\xa3\xf0\x9f\x8d\xa3')
comp.decompress(b'\xf0\x9f\x8d\xa3\xf0\x9f\x8d\xa3')




def mylzma(data):
    comp = lzma.LZMADecompressor()
    #comp.decompress(b'\xf0\x9f\x8d\xa3')
    return comp.decompress(data)

mylzma(b'\xf0\x9f\x8d\xa3\xf0\x9f\x8d\xa3')



def mylzma(data):
    #comp = lzma.LZMADecompressor()
    #comp.
