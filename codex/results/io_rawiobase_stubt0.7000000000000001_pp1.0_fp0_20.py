import io
class File(io.RawIOBase):
    """ File_proxy is a proxy object that handles the
        communication with a real file object in another process.
        It can be used as a drop-in replacement for the real file object.

        File_proxy class is not threadsafe.
    """
    def __init__(self, conn):
        self.conn = conn
        self.name = conn.recv()
        self.mode = conn.recv()
        self.pid = conn.recv()
        self.conn.send(True)

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        self.close()

    def writable(self):
        return 'w' in self.mode or 'a' in self.mode

    def readable(self):
        return True

    def seekable(self):
        return True

    def close(self):
        self.conn.send(('close',))
        self.conn.recv()

    def fileno(self):
        self.conn.send(('fileno',))
        return self.
