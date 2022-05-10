import io
class File(io.RawIOBase):
    """文件类"""
    # mode = ''
    def __init__(self, file):
        self.file = file
        self.closed = False
        self.mode = ''
        self.pos = 0
        self.softspace = 0

    def open(self, file, mode='r'):
        """打开一个文件，返回文件对象
        如果打开失败，会引发 IOError 异常，具体异常信息在 exception 成员中。
        否则，返回一个文件对象。
        """
        try:
            if not self.closed:
                raise ValueError('I/O operation on closed file')
            if mode not in ('r', 'w', 'a'):
                raise ValueError
        except ValueError:
            print('ValueError
