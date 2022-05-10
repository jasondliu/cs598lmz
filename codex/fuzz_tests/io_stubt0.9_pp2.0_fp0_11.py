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
del view

_IO_struct_getline(p, -1)
gc.collect()
print(len(_IO_list_all))
