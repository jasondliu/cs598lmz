import io
class File(io.RawIOBase):
    def __init__(self, path, mode='r'):
        if mode in 'wa':
            self._elm_file = elm.Elm_Fileselector_Entry.go_to_parent(path)
        else:
            self._elm_file = elm.Elm_Fileselector_Entry.go_to_child(path)

    def close(self):
        self._elm_file.destroy()

    def read(self, n=-1):
        return self._elm_file.read(n)

    def readinto(self, b):
        data = self.read(len(b))
        if data:
            b[:len(data)] = data
            return len(data)
        return 0

    def readable(self):
        return True

    def seek(self, offset, whence=0):
        return self._elm_file.seek(offset, whence)

    def seekable(self):
        return True

    def tell(self):
        return self._elm_file.tell()

    def writable
