from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# LZMA
# LZMAFile(fileobj=None, mode=None, format=None, check=-1, preset=None, filters=None)
# LZMAFile.compress(data, format=FORMAT_XZ, check=-1, preset=None, filters=None)
# LZMAFile.decompress(data)

# LZMA2
# LZMA2File(fileobj=None, mode=None, format=None, check=-1, preset=None, filters=None)
# LZMA2File.compress(data, format=FORMAT_XZ, check=-1, preset=None, filters=None)
# LZMA2File.decompress(data)

# BZIP2
# BZ2File(name=None, mode=None, buffering=0, compresslevel=9)
# BZ2File.compress(data, compresslevel=9)
# BZ2File.decompress(data)

# ZIP
# ZipFile(file, mode='r', compression=
