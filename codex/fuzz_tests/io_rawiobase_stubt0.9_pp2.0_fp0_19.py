import io
class File(io.RawIOBase):
    def read(self, n=-1):
        return b''

import errno
def _eintr_retry_call(func, *args):
    while True:
        try:
            return func(*args)
        except (OSError, IOError) as e:
            if e.errno == errno.EINTR:
                continue
            raise

_sendfile_use_sendfile = True
def _sendfile_use_sendfile_check():
    global _sendfile_use_sendfile
    _sendfile_use_sendfile = False
    from socket import socketpair
    sock1, sock2 = socketpair()
    try:
        fd = sock1.fileno()
        try:
            _eintr_retry_call(sendfile, fd, fd, 0, 1)
        except AttributeError:
            pass
        except OSError as e:
            if e.errno != errno.ENOSYS:
                raise e
    finally:
        sock1.close()
        sock2.close()

