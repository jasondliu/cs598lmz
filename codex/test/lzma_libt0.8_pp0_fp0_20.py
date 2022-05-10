import lzma
lzma.open = lzma.LZMAFile
import tarfile
import zipfile

from encodings import idna

def __scale__(d):
    if isinstance(d, dict):
        return dict(map(lambda k: (k, __scale__(d[k])), d))
    if isinstance(d, list):
        return list(map(lambda x: __scale__(x), d))
    if isinstance(d, tuple):
        return tuple(map(lambda x: __scale__(x), d))
    if isinstance(d, bytes):
        return d.decode()
    return d

def __rescale__(d):
    if isinstance(d, dict):
        return dict(map(lambda k: (k, __rescale__(d[k])), d))
    if isinstance(d, list):
        return list(map(lambda x: __rescale__(x), d))
    if isinstance(d, tuple):
        return tuple(map(lambda x: __rescale__(x), d))
   
