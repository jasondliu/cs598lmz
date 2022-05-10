import mmap
# Test mmap.mmap
# import binascii
import codecs


# need a single point for other code to access mmap
class mmapData(object):
    def __init__(self):
        self.data = None

    def setData(self, data):
        self.data = data

dummy = mmapData()


def hexdump(s):
    return codecs.encode(s, 'hex_codec').decode('ascii')


def init_mmap(file1, file2):
    # print('%d\n' % len(data))
    # this looks interesting but works only on Windows:
    # https://docs.microsoft.com/en-us/windows/win32/memory/using-memory-mapped-files
    # https://www.geeksforgeeks.org/mmap-function-in-python/

    # map the binary file into memory
    ln1 = os.path.getsize(file1)
    ln2 = os.path.getsize(file2)
