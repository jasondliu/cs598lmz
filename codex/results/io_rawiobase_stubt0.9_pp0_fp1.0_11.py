import io
class File(io.RawIOBase):
    def readable(self):
        pass

    def readinto(self, b):
        pass

if __name__=="__main__":
    test = File()
    print(test.readable())
# $ python3 io_subclass.py
# True
