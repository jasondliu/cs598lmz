import io
# Test io.RawIOBase for issue #17893

try:
    io.RawIOBase
    import socket
    import _testcapi
    try:
        import threading
    except ImportError:
        threading = None
except ImportError:
    import sys
    sys.exit(0)

