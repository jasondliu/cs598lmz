import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
# if the buffer is not unlinked, this is a memory leak.

del view # make sure the contents of the buffer are gone

if __name__ == '__main__':
    import gc
    for i in range(5):
        gc.collect()
    print('Done')
