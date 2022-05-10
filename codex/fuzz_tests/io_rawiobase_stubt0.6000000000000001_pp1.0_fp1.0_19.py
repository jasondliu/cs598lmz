import io
class File(io.RawIOBase):
    def __init__(self, path):
        self._path = path
        self._file = None
    def open(self):
        self._file = open(self._path, 'rb')
    def close(self):
        if self._file:
            self._file.close()
    def read(self, n):
        return self._file.read(n)
</code>
<code>File</code> is a simple wrapper around <code>open</code>.
I can run <code>File</code> as a thread:
<code>class FileThread(threading.Thread):
    def __init__(self, file, n):
        self._file = file
        self._n = n
        super().__init__()
    def run(self):
        self._file.open()
        self._file.read(self._n)
        self._file.close()

file = File('file.txt')
file_thread = FileThread(file, 1024)
file_thread.start()
file_thread.join()
</code>
If I want to
