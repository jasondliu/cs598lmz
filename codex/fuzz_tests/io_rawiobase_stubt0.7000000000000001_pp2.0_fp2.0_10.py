import io
class File(io.RawIOBase):
    def __init__(self, fd):
        self.fd = fd
        self.writable = fd.writable
        self.readable = fd.readable

    def close(self) -> None:
        self.fd.close()

    def fileno(self) -> int:
        return self.fd.fileno()

    def readinto(self, b: bytearray) -> int:
        return self.fd.readinto(b)

    def write(self, b: AnyStr) -> int:
        return self.fd.write(b)

    def seek(self, offset: int, whence: int = 0) -> int:
        return self.fd.seek(offset, whence)

class WebSocketFile(File):
    def __init__(self, ws):
        self.ws = ws
        super().__init__(ws.sock)
        self.incoming_frame = bytearray()
        self.outgoing_frame = bytearray()

    def readinto(self, b: bytearray) ->
