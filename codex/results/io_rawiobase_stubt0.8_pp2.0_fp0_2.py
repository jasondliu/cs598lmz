import io
class File(io.RawIOBase):
    """
    分页读取大文件
    """
    def __init__(self, file, block_size=io.DEFAULT_BUFFER_SIZE):
        self.file = file
        self.block_size = block_size

    def read(self, n=-1):
        res = []
        if n < 0:
            while True:
                data = self.file.read(self.block_size)
                res.append(data)
                if len(data) < self.block_size:
                    break
            return b''.join(res)
        else:
            block = n // self.block_size
            for i in range(block):
                data = self.file.read(self.block_size)
                res.append(data)
            remain = n - block * self.block_size
            res.append(self.file.read(remain))
            return b''.join(res)

def file_md5(f):
    """
    获取文件的md5
