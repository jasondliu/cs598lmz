from lzma import LZMADecompressor
LZMADecompressor().decompress(b)

del b

jpgs = glob.glob(os.path.expanduser("./fata_morgana/FC-LKI/*.jpg"))

for jpg in jpgs:
    os.unlink(jpg)
