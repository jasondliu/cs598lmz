import io
class File(io.RawIOBase):#如果用户使用自己的缓存对象，而不是与文件系统的连接，
#io.BytesIO类或io.StringIO类，则必须为这些对象实现上层文件接口
    def __init__(self, filename, mode='r', buffering=-1):
        self.filename = filename
        self.access_mode = mode
        self.buffer = buffering

    def write(self, data):
        print('Write data to file:{}'.format(self.filename))

    def read(self, nbytes):
        print('read() not implemented')

    def readline(self):
        print('readline() not implemented')


file = File('filename', 'w')
file.write('Some text')


# 覆盖上层基
