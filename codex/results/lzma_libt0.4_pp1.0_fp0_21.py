import lzma
lzma.open

# @lru_cache(maxsize=None)
class LzmaCompress:
    def __init__(self,level=9):
        self.level = level
    def __call__(self,data):
        return lzma.compress(data,level=self.level)
    def __repr__(self):
        return f'LzmaCompress(level={self.level})'

# @lru_cache(maxsize=None)
class LzmaDecompress:
    def __init__(self,level=9):
        self.level = level
    def __call__(self,data):
        return lzma.decompress(data)
    def __repr__(self):
        return f'LzmaDecompress(level={self.level})'

# @lru_cache(maxsize=None)
class BrotliCompress:
    def __init__(self,level=9):
        self.level = level
    def __call__(self,data):
        return bro
