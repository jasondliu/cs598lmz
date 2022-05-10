from lzma import LZMADecompressor
LZMADecompressor.concatenate = lambda _, data: b"\x00".join(data)
decompress = LZMADecompressor(auto_decode=False).decompress

class Archive:
    def __init__(self, name):
        self.name = name
        self.files = {}
        try: fp = open(name, "rb")
        except: return
        nfiles, = unpack("<H", fp.read(2))
        self.index = unpack(f"<{nfiles}I", fp.read(nfiles*4))
        fp.close()

    def __getitem__(self, key):
        path = join(self.name + ".d", key)
        try:
            item = self.files[path]
        except KeyError:
            fp = open(path, "rb")
            data = decompress(fp.read())
            fp.close()
            item = self.files[path] = BytesIO(data)
        return item

def pakopen(fn, mode="
