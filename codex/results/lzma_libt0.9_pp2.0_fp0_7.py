import lzma
lzmaFile = open("text.xz", "wb")
lzmaFile.write(lzma.compress(data))
lzmaFile.close()

print("LZMA compression is done.")
