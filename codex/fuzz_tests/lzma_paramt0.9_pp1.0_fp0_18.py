from lzma import LZMADecompressor
LZMADecompressor().decompress(lzma_file)
with open("hoge.txt.lzma", 'rb') as f:
    lzma_file = f.read()
    text_file = lzma.decompress(lzma_file)
text = codecs.decode(text_file, "eucjp", "ignore")
print(text)
