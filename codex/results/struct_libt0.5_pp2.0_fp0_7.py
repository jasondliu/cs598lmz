import _struct

class KVStore:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
        self.open()

    def open(self):
        self.file = open(self.filename, "r+b")
        self.file.seek(0, 2)
        self.size = self.file.tell()
        self.file.seek(0)

        self.entries = {}
        self.keys = []
        self.values = []
        self.load()

    def load(self):
        for i in range(0, self.size, 8):
            self.file.seek(i)
            key, value = _struct.unpack("<II", self.file.read(8))

            self.entries[key] = value
            self.keys.append(key)
            self.values.append(value)

    def close(self):
        self.file.close()

    def __getitem__(self, key):
        return self.entries[key]

    def __setitem__(
