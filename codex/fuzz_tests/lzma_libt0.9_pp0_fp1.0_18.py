import lzma
lzma.LZMADecompressor


# Try bz2
import bz2
bz2.BZ2Decompressor()


# Try unrar
try:
    import unrar
except ImportError:
    class Unrar(object):
        open = None
        unrar = None

    unrar = Unrar()
else:
    try:
        # Workaround for missing RarFile method declaration in unrar/rarfile.py
        # https://github.com/markokr/rarfile/issues/52
        from unrar.rarfile import RarFile, RarInfo
        import errno

        if 'getinfo' not in RarFile.__dict__:
            def getinfo(self, fn, extract=False):
                try:
                    src_rarfile_obj = self._open(fn)
                except IOError as e:
                    if e.errno == errno.ENOENT:
                        return None
                    raise

                if extract:
                    self._extract(src_rarfile_obj)
                return RarInfo(src_rar
