import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0
    def read(self, n=-1):
        self.file.seek(self.offset)
        chunk = self.file.read(n)
        self.offset += len(chunk)
        return chunk

def get_file_size(file_obj):
    file_obj.seek(0, os.SEEK_END)
    size = file_obj.tell()
    file_obj.seek(0)
    return size

def get_chunk(file_obj, chunk_size, offset):
    file_obj.seek(offset)
    return file_obj.read(chunk_size)

def get_chunk_md5(file_obj, chunk_size, offset):
    return hashlib.md5(get_chunk(file_obj, chunk_size, offset)).hexdigest()

def get_file_md5(file_obj):
    return hashlib.md5(file_obj.read()).hexdigest()


