import mmap
# Test mmap.mmap to see if it can be used
try:
    m = mmap.mmap(-1, 1)
    m.write('\0')
    m.seek(0)
    if not m.read(1):
        raise ValueError
except (ValueError, mmap.error):
    mmap = None

try:
    import fcntl
except ImportError:
    fcntl = None

try:
    import struct
except ImportError:
    struct = None

try:
    import termios
except ImportError:
    termios = None

try:
    WindowsError
except NameError:
    class WindowsError(Exception):
        pass

try:
    import msvcrt
except ImportError:
    msvcrt = None

