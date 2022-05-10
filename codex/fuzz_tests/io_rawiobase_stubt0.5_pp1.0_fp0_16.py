import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.file = io.open(filename, 'rb')
        self.filename = filename
        self.size = os.fstat(self.file.fileno()).st_size
        self.read = self.file.read
        self.seek = self.file.seek
        self.tell = self.file.tell
        self.close = self.file.close
        self.__len__ = lambda self: self.size

def _get_file_size(file_object):
    if hasattr(file_object, 'size'):
        return file_object.size
    if hasattr(file_object, 'name'):
        try:
            return os.fstat(file_object.fileno()).st_size
        except:
            pass
    if hasattr(file_object, 'tell') and hasattr(file_object, 'seek'):
        pos = file_object.tell()
        file_object.seek(0, 2)  # seek end
        size = file_object.tell()
       
