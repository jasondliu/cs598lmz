from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

#bz2
from bz2 import decompress, BZ2Decompressor
decompress(data)
decompressor = BZ2Decompressor()
decompressor.decompress(data)
decompressor.decompress(more_data)

#zlib
from zlib import decompress, decompressobj
decompress(data)
decompressobj().decompress(data)

#zip
from zipfile import ZipFile
zip = ZipFile(zip_path, 'r')
zip.extractall()

#tar
from tarfile import TarFile
tar = TarFile(tar_path, 'r')
tar.extractall()

#gzip
from gzip import decompress, GzipFile
decompress(data)
gzip_file = GzipFile(filename, 'r')
gzip_file.read()
gzip_file.read(size)
gzip_file.readlines()
gzip_file.seek(offset)
gzip_file.tell()
gzip_file
