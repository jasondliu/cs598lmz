import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r'):
        self._name = name
        self._mode = mode
    def read(self, size=-1):
        return 'file'

class FileInfo(object):
    def __init__(self, name, *args):
        self.name = name
        self.args = args

class FileInfoList(list):
    def __init__(self, name):
        self.name = name
    def __getitem__(self, index):
        return FileInfo(self.name, index)

class FileList(list):
    def __init__(self, name):
        self.name = name

class FileListInfo(object):
    def __init__(self, name):
        self.name = name
    def __getitem__(self, index):
        return FileList(self.name)

class FileStorage(object):
    def __init__(self, name, mode='r', *args):
        self.name = name
        self.mode = mode
        self.args = args
