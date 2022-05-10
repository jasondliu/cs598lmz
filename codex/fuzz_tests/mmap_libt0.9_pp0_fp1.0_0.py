import mmap
import struct
from os import path

from Crypto.Cipher import AES

from oblytils import utility, aesutils

__builtin_loaded = False

class MMapReader():
    def __init__(self, file_path, block_size=8192):
        self.file_path = file_path
        self.block_size = block_size

    def __enter__(self):
        self.fd = os.open(self.file_path, os.O_RDONLY)
        self.mm = mmap.mmap(self.fd, 0, flags=mmap.MAP_SHARED, prot=mmap.PROT_READ)
        return self

    def __exit__(self, *exc_info):
        self.mm.close()
        os.close(self.fd)
        return False

    def read(self, offset, length):
        ret = bytearray()
        while length > 0:
            to_copy = min(self.block_size, length)
            self.mm.seek(offset)
           
