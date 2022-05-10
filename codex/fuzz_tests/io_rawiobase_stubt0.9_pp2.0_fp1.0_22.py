import io
class File(io.RawIOBase):
    def fileno(self):
        return self.fd

    def close(self):
        if self.fd != -1:
            os.close(self.fd)
            self.fd = -1

    def isatty(self):
        try:
            return os.isatty(self.fd)
        except OSError:
            return False

import os
def _setmode(fd, mode):
    if mode == os.O_TEXT:
        return
    fd = fd

    original_mode = fd.mode
