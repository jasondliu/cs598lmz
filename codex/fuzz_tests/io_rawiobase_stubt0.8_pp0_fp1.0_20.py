import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.file = open(filename, 'rb')
        self.blocksize = 512
    def read(self, blocksize=0):
        if blocksize == 0:
            return self.file.read()
        return self.file.read(blocksize)
    def readinto(self, buf):
        buf[:512] = self.file.read(512)
        return 512
    def close(self):
        self.file.close()

def generate_drive_header(sector_count, sector_size=512):
    size = sector_count * sector_size
    return b'\xF8' + b'\xFF'*10 + struct.pack('<H', sector_count) + b'\x01' + b'\xF8' + b'\xFF'*6 + bytes([sector_size]) + b'\xF8'*488
