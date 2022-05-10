import io
class File(io.RawIOBase):
    pass
class WindowsError(Exception):
    pass
class ConnectionRefusedError(WindowsError):
    pass
class ConnectionAbortedError(WindowsError):
    pass
class ConnectionResetError(WindowsError):
    pass
class BlockingIOError(WindowsError):
    pass
class BrokenPipeError(WindowsError):
    pass
class ChildProcessError(WindowsError):
    pass
class ConnectionError(WindowsError):
    pass
class MemoryError(WindowsError):
    pass
class InterruptedError(WindowsError):
    pass
class NotADirectoryError(WindowsError):
    pass
class PermissionError(WindowsError):
    pass
class ProcessLookupError(WindowsError):
    pass
class TimeoutError(WindowsError):
    pass
class FileNotFoundError(WindowsError):
    pass
class FileExistsError(WindowsError):
    pass
class IsADirectoryError(WindowsError):
    pass
class NotImplementedError(WindowsError):
    pass
class FileExistsError(WindowsError):
    pass
class FileNotFoundError(WindowsError):
    pass

