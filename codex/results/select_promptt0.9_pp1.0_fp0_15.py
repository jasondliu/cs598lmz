import select
# Test select.select with descriptors that read() will not block.
# Most of this is used to bypass fcntl on Linux, which doesn't allow these
# tests with nonblocking sockets (tested later).  The C side is a
# half-duplex (but full-duplex in select) pipe where calling write() would
# fail; read() is allowed though.
# Refer to Modules/posixmodule.c for details.
import socket, sys
if '__pypy__' in sys.builtin_module_names:
    raise skip('Sockets not supported on PyPy')
import _posixsubprocess
UNDEFINED = object()
devnull = open('/dev/null', 'wb')
fd = os.dup(devnull.fileno())
devnull.close()
os.write(fd, b'stuff\n')
os.lseek(fd, 0, 0)
r, w, x = select.select([fd], [], [], 1.0)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
r, w, x
