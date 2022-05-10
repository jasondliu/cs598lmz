import io
class File(io.RawIOBase):
    def fileno(self):
        return os.open(self.name, self.flags, self.mode)

    def __init__(self, name, mode="rb", buffering=None):
        self.mode = mode
        self.name = name
        self.flags = 0
        flag = os.O_LARGEFILE | os.O_NOCTTY

        if mode.startswith("r"):
            flag |= os.O_RDONLY
            self.flags = os.O_RDONLY

        elif mode.startswith("w"):
            if not os.path.exists(name):
                open(name, "w").close()
            flag |= os.O_RDWR | os.O_TRUNC
            self.flags = os.O_RDWR | os.O_TRUNC

        elif mode.startswith("a"):
            flag |= os.O_RDWR|os.O_APPEND
            self.flags = os.O_RDWR|os.O_APPEND

        self.fd
