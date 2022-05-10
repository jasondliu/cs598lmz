import io
class File(io.RawIOBase):
    '''Wrapper around file handler to provide file pointer'''
    def __init__(self,f):
        io.RawIOBase.__init__(self)
        self.file = f

    def tell(self):
        self.file.seek(0, io.SEEK_CUR)
    def read(self, n=0):
        return self.file.read(n)

    def seek(self, offset, whence=0):
        return self.file.seek(offset)

    def write(self,b):
        return self.file.write(b)

    def readinto(self, b):
        return self.file.readinto(b)

    def seekable(self):
        return True

def download(url,path=None,out=None,filename=None,job_name=None,chunk_size=1024):
    '''
    This routine downloads file from remote server

    Parameters:
    -------------------------------------------
    url: link of file to be downloaded
    path: path where to store the files
    out: string to write on console
   
