import io
class File(io.RawIOBase):
    def __init__(self, archive, file_info, file_obj=None):
        self._archive = archive
        self._file_info = file_info
        if file_obj:
            self._file_obj = file_obj
        else:
            self._file_obj = self._archive._get_file_obj(file_info)
        self._closed = False
    
    def read(self, size=-1):
        if size == -1:
            return self._file_obj.read()
        return self._file_obj.read(size)
    
    def seekable(self):
        return True
        
    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self._file_obj.seek(offset)
        elif whence == io.SEEK_CUR:
            self._file_obj.seek(self._file_obj.tell() + offset)
        elif whence == io.SEEK_END:
            self._file_obj.seek(self._file_info
