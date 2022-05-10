import io
class File(io.RawIOBase):
    __slots__ = ['_close_fd']
    def __init__(self, close_fd):
        _close_fd = bool(close_fd)
        if _close_fd:
            print('This is running')
        print('These words never show up')




if __name__ == '__main__':
   File(True)
