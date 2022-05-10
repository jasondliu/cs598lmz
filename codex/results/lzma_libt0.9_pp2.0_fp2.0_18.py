import lzma
lzma.LZMAFILE_FORMAT_RAW
 
lofile = open("./README.md", "rb")
cfile = open("./README.md.xz", "wb")
comp = lzma.LZMACompressor()
comp.format = lzma.LZMAFILE_FORMAT_RAW
# comp.compress(char)
print(comp.compress(lofile.read(1024)))
print(comp.compress(b'a'))
print(comp.flush())

lofile.close()
cfile.close()

with open("./README.md", "rb") as f1:
    with open("./README.md.xz", "wb") as f2:
        comp = lzma.LZMACompressor()
        for char in f1.read(1024):
            comp.compress(char)
        comp.flush()


# calculate the lzma csum of a file
with open("./README.md.xz", "rb") as f2:
