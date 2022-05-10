import io
class File(io.RawIOBase):
    """ Shared file object
    """
    def __init__(self, name, mode='rb', buffering=-1, encoding=None,
                 errors=None, newline=None, closefd=True, opener=None):
        if not (mode == 'rb' or mode == 'wb'):
            raise ValueError('open for read and write')
        if 'a' in mode or '+' in mode:
            raise ValueError('not append mode')
        if buffering == 0:
            raise ValueError('must have positive non-zero buffering')
        self.name = name
        self.mode = mode
        if hasattr(self, '_sock'):
            return
        self._sock = open(name, mode, buffering, encoding, errors, newline)

    def close(self):
        """docstring for close"""
        if hasattr(self, '_sock'):
            self._sock.close()

class Netfile(File):
    """docstring for Netfile"""
    def __init__(self, *args, **kwargs):

