import lzma
lzma.open

# import rarfile
# rarfile.RarFile

# import tarfile
# tarfile.TarFile

# import zipfile
# zipfile.ZipFile

# import zlib
# zlib.decompress


def read_raw(filename):
    with open(filename, 'rb') as f:
        return f.read()


def read_text(filename):
    with open(filename, 'r') as f:
        return f.read()
