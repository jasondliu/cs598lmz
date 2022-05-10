import lzma
# Test LZMADecompressor
try:
    lzma.LZMADecompressor()
except:
    print("Error: LZMADecompressor object not created")
    sys.exit(1)

# Test LZMADecompressor.decompress()
try:
    lzma.LZMADecompressor().decompress(b'x\x9c')
except:
    print("Error: LZMADecompressor.decompress() not working")
