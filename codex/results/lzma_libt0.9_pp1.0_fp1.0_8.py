import lzma
lzma = lzma.LZMAFile('compressed.lzma', 'wb', preset=9)
lzma.write(data)
lzma.close()

lzma = lzma.LZMAFile('compressed.lzma', 'rb')
print(len(lzma.read()))

lzma = lzma.LZMAFile('compressed.lzma', 'rb')
data_lzma = json.load(lzma)
for x in data_lzma:
    print(x)
