import io
class File(io.RawIOBase):
    def __init__(self):
        print('init')
        self.data=b''

    def write(self, data):
        print('write')
        if len(data) > 14:
            raise Exception("大于14")
        print("write%s"%data)
        if len(data):
            self.data += data

    def read(self):
        print('read')
 
