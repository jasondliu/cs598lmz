import lzma
# Test LZMADecompressor class
#

def main():
    dec = lzma.LZMADecompressor()

    data = open('lzma_corpus', 'rb').read()

    data = dec.decompress(data)

    print(dec.eof)

main()
