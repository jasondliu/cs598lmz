import io
class File(io.RawIOBase):
    @property
    def name(self):
        return self.__class__.__name__

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

stdin = File()
stdout = File()
stderr = File()
