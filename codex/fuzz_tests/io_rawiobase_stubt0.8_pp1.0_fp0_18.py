import io
class File(io.RawIOBase):
    def __init__(self, path: str):
        self.path = path
        self.file = open(path, 'rb')

    def close(self):
        self.file.close()

    def read(self):
        return self.file.read()


class SymPyC(Compiler):
    def __init__(self, requires: Sequence[File] = None, description: str = None,
                 name: str = None, cmd: str = None):
        self.includes = []
        self.defines = []
        self.files = []
        super().__init__(requires=requires, description=description, name=name, cmd=cmd)

    def add_include(self, include: Union[str, File]):
        if isinstance(include, str):
            include = File(include)
        self.includes.append(include)

    def add_define(self, define: str):
        self.defines.append(define)

    def add_file(self, file: File):
        if isinstance(file, str):
            file = File
