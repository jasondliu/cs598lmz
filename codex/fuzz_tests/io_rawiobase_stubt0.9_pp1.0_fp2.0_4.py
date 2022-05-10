import io
class File(io.RawIOBase):
    def __init__(self, name, mode='rb', closefd=True):
        '''
        open file
        '''
        self.fd = os.open(name, _pyio.to_mode_string(mode, "r"), 0777)
        self._mode = mode
        self._closefd = closefd
    def open(self, name, mode='rb', buffering=None, encoding=None,
        errors=None, newline=None, closefd=True, opener=None):
        """注意，打开文件后 确保 偏移量必须被拖出去默认值，所以在close 之前调用 flush() 来将文件游标定位到末尾
        """
        self.fd = os.open(name, _pyio.to_mode_string(mode, 'r'), 0777)
        self
