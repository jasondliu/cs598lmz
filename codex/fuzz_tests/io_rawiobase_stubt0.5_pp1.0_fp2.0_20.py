import io
class File(io.RawIOBase):
    def __init__(self, file, *args, **kwargs):
        self.file = file
        super(File, self).__init__(*args, **kwargs)

    def read(self, n=-1):
        return self.file.read(n)

    def close(self):
        if self.file is not None:
            self.file.close()
            self.file = None

class FileIterWrapper(object):
    def __init__(self, flo):
        self.flo = flo

    def __iter__(self):
        return self

    def next(self):
        data = self.flo.read(CHUNK_SIZE)
        if data:
            return data
        else:
            raise StopIteration

class S3Transfer(object):
    """
    The S3Transfer object is a context manager that allows you to
    transfer files to and from S3.  It uses the S3 client object to
    make requests to S3.  The transfer commands are asynchronous by
    default.  This allows you to use the context manager in a
