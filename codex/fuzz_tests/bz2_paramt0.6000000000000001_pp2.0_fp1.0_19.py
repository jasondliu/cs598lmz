from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = Decompressor.decompress

from gzip import GzipFile
GzipFile._read_eof = Decompressor._read_eof
GzipFile._read_gzip_header = Decompressor._read_gzip_header
GzipFile.read = Decompressor.read
GzipFile.read1 = Decompressor.read1
GzipFile.readinto = Decompressor.readinto
GzipFile.readline = Decompressor.readline
GzipFile.readlines = Decompressor.readlines
GzipFile.decompress = Decompressor.decompress
GzipFile.__init__ = Decompressor.__init__
GzipFile.__del__ = Decompressor.__del__

from zlib import decompressobj
decompressobj.decompress = Decompressor.decompress

def patch():
    '''
    Patches the decompressors to use the new Decompressor class.
    '''
    pass

def unpatch():
    '''
    Unpatches the decompressors to
