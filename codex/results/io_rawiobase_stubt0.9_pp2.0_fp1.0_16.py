import io
class File(io.RawIOBase):
    """
    File(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    类似open, 但不使用closefd=False不是很明白
    """
    def __init__(self):
        print("__init__")

    def _init(self, name, mode = 'r', buffering = -1, encoding = None,
              errors = None, newline = None, closefd = True, opener = None):
        print("_init:", name, mode, buffering, encoding, errors, newline, closefd, opener)
        return super().__init__(name, mode, buffering, encoding, errors, newline, closefd, opener)

    def mkFile(self, fp):

        #初始化File对象
        f = File()
        f._init(fp, 'r', -1, None, None, None, 1, None)     #如果 open(fp, '
