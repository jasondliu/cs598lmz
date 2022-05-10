import lzma
lzma.LZMAError

# This is a workaround for https://bugs.python.org/issue29288
# It will be removed when we drop support for Python 3.5
if sys.version_info[:2] == (3, 5):
    import ssl
    ssl.SSLError

# This is a workaround for https://bugs.python.org/issue29288
# It will be removed when we drop support for Python 3.5
if sys.version_info[:2] == (3, 5):
    import _ssl
    _ssl.SSLError

# This is a workaround for https://bugs.python.org/issue29288
# It will be removed when we drop support for Python 3.5
if sys.version_info[:2] == (3, 5):
    import _socket
    _socket.error

# This is a workaround for https://bugs.python.org/issue29288
# It will be removed when we drop support for Python 3.5
if sys.version_info[:2] == (3, 5):
    import _socket

