import io
class File(io.RawIOBase):
    """
    +----------------+
    |  文件对象的操作 |
    +----------------+
    """
    def __init__(self, file):
        """
        :param file: 文件对象操作
        :return:
        """
        self.file = file

    def write(self, x):
        """
        写入文件
        :param x:
        :return:
        """
        if x is None:
            return 0
        n = len(x)
        n = self.file.write(x)
        return n

    def read(self, n=-1):
        """
        读取文件
        :param n:
        :return:
        """
        if n is None:
            n = -1
        return self.file.read(n)

    def readable(self):
        """
        是否可读
        :return:
        """
        return self.file.
