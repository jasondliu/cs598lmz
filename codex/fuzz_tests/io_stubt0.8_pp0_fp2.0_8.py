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

while True:
    # Open the file again
    f = open("view.txt", "rb")

    # We don't want to lose the original value of the 'view' pointer
    old_view = view
    eval(compile(f.read(), "view.txt", "exec"))
    f.close()

    # Restore the original value of the 'view' pointer
    view = old_view
