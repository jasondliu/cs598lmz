import io
class File(io.RawIOBase):

    def readinto(self,b):
        print("readinto")
        return 0

    def readable(self):
        return True

    def write(self,b):
        print("write")
        return len(b)
        #raise NotImplementedError
    def writable(self):
        return True

aFile = File()

print(aFile.readable())

#aFile.readinto(b"")

print(aFile.writable())

#aFile.write(b"")


import io

class BaseConvert(io.RawIOBase):
    def __init__(self, source):
        self._source = source

    def readable(self):
        return self._source.readable()

    #def writable(self):
    #    return self._source.writable()



class Binary2Ascii(BaseConvert):

    def write(self, b):
        length = len(b)
        ascii_data = []
        for i in b:
            ascii_data.append("{:08
