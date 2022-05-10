from lzma import LZMADecompressor
LZMADecompressor.flush = lambda self: bytes()

MIME_TO_TYPE = {
    "application/x-xz": "xz",
    "application/x-bzip2": "bz2",
    "application/zip": "zip",
}


def is_zipfile(filename):
    return filename.endswith(".zip")


def is_xzfile(filename):
    return filename.endswith(".xz")


def is_bzipfile(filename):
    return filename.endswith(".bz2")


def get_opener(filename, mode="rb"):
    if is_xzfile(filename):
        return lzma.open

    if is_zipfile(filename):
        return zipfile.ZipFile

    if is_bzipfile(filename):
        return bz2.BZ2File

    return open


def get_reader(filename, **kwargs):
    if is_xzfile(filename):
        return LZMADecompressor(**kwargs)

    if is_zipfile(
