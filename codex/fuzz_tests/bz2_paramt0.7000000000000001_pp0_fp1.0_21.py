from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# bz2.decompress()
# bz2.BZ2Decompressor()

# bz2.BZ2Decompressor().decompress(bz2_data)

# lzma
import lzma
lzma.decompress(lzma_data)

# lzma.decompress()
# lzma.LZMADecompressor()

# lzma.LZMADecompressor().decompress(lzma_data)

# zipfile
import zipfile
with zipfile.ZipFile(zip_file) as zf:
    zf.printdir()
    with zf.open('file2.txt') as f:
        file2_data = f.read()
print(file2_data.decode('utf-8'))

# zipfile.ZipFile()
# zipfile.ZipFile().printdir()
# zipfile.ZipFile().namelist()
# zipfile.ZipFile().open()

# zip
