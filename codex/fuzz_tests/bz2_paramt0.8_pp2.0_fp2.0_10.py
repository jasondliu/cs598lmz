from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = patched_bz2_decompress
# TODO: Replace it when python3.8 is the default python on Trusty
from  bz2file import BZ2File
BZ2File._read_compressed_chunk_pre_python38 = patched_bz2file_read_compressed_chunk_pre_python38

def open_func(path):
    if not hasattr(builtins, 'open'):
        def open_func(path, mode='r'):
            with BZ2File(path, mode + 'b') as f:
                if 'b' not in mode:
                    f = io.TextIOWrapper(f)
                return f
        return open_func
    else:
        return builtins.open

class Bz2ExtModule(Extension):
    """
    A module for handling bz2 files.
    """

    def __init__(self):
        super().__init__("bz2", prefix="bz2")

    def source(self, source_path):
        self.source_
