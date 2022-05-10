import lzma
lzma.DECOMPRESS_BUFFER_SIZE = 2 ** 16

# The following structure is built from the following markdown file:
# https://raw.githubusercontent.com/dlang/dlang.org/master/druntime/phobos/std/zlib/zip.d

class Struct:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

class ZipFileHeader(Struct):
    pass

class ZipLocalFileHeader(Struct):
    pass

class ZipCentralDirectoryHeader(Struct):
    pass

class ZipEndOfCentralDirectoryHeader(Struct):
    pass

class ZipArchive(Struct):
    pass

def readStruct(f, struct):
    return struct._make(struct._fields_type(f.read(struct.size)))

def readString(f, size):
    return f.read(size).rstrip("\x00")

# ZipFileHeader
ZipFileHeader._fields_type = StructTuple(
    readUByte,  #
