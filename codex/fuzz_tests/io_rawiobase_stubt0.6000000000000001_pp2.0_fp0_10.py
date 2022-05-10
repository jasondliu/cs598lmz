import io
class File(io.RawIOBase):
    pass

class Socket(io.RawIOBase):
    pass

class SocketStream(io.RawIOBase):
    pass

class SSLIO(io.RawIOBase):
    pass

class Pipe(io.RawIOBase):
    pass

class Process(io.RawIOBase):
    pass

class ProcessStream(io.RawIOBase):
    pass

class StreamWriter(io.RawIOBase):
    pass

class StreamReader(io.RawIOBase):
    pass

class BufferWriter(io.RawIOBase):
    pass

class BufferReader(io.RawIOBase):
    pass

class Stdio(io.RawIOBase):
    pass

class StdioStream(io.RawIOBase):
    pass

class StdioPipe(io.RawIOBase):
    pass

class StdioStreamPipe(io.RawIOBase):
    pass

class StdioBuffer(io.RawIOBase):
    pass

class StdioBufferPipe(io.RawIOBase):
    pass
