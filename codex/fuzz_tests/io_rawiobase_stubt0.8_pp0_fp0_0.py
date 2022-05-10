import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.length = os.fstat(file.fileno()).st_size

    def read(self, size=-1):
        if self.length == 0:
            return b''
        if size < 0:
            size = self.length
        elif size > self.length:
            size = self.length
        self.length -= size
        return os.read(self.file.fileno(), size)

    def readable(self):
        return True

def get_zip_data(zip_file):
    z = zipfile.ZipFile(zip_file)
    names = z.namelist()
    data = {n: z.read(n) for n in names}
    return data

def get_file_data(file):
    return {file: File(file)}

def get_data(path):
    try:
        return get_zip_data(path)
    except zipfile.BadZipFile:
        return get_file_data(path)

def get
