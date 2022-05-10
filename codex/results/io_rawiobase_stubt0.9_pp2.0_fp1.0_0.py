import io
class File(io.RawIOBase):

    def __init__(self, fileName, mode='r'):
        self.fileName = fileName
        self.mode = mode

    def fileno():
        return os.open(self.fileName)

    def close():
        pass

    def read(size):
        pass
</code>


A:

Checking out the Docs for <code>io.RawIOBase</code>, I noticed that the <code>fileno</code> method returns an "integer." So, I wrapped the <code>self.fileName</code> in an <code>int</code> and all works now.

