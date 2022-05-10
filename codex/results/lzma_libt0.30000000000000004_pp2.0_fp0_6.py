import lzma
lzma.LZMAError:
    print('lzma is not available.  Using zip instead.')
    import zipfile
    class LZMAFile(zipfile.ZipFile):
        def __init__(self, filename, mode="r", *args, **kwargs):
            if mode not in ("r", "w"):
                raise ValueError("mode must be 'r' or 'w'")
            zipfile.ZipFile.__init__(self, filename, mode, zipfile.ZIP_DEFLATED, *args, **kwargs)
        def read(self, n=-1):
            return zipfile.ZipFile.read(self, n)
        def write(self, b):
            return zipfile.ZipFile.write(self, b)
        def tell(self):
            return zipfile.ZipFile.tell(self)
        def seek(self, offset, whence=0):
            return zipfile.ZipFile.seek(self, offset, whence)
        def close(self):
            return zipfile.ZipFile.close(self)
        def __next
