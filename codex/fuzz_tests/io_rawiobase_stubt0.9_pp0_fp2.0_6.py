import io
class File(io.RawIOBase):
    def __init__(self, system_state, path, profile):
        if len(system_state.file_info) > 0 and path in system_state.file_info:
            self.file_info = system_state.file_info[path]
            self.size = self.file_info.size
        else:
            self.file_info = file_info.FileInfo()
            self.size = profile.file_size(path)
            system_state.file_info[path] = self.file_info

    def readinto(self, b):
        self.file_info.bytes_read += len(b)
        return len(b)

    def seekable(self):
        return False

    def write(self, b):
        self.file_info.bytes_written += len(b)
        return len(b)

    def seek(self, i, io):
        assert 0

    def tell(self):
        assert 0
