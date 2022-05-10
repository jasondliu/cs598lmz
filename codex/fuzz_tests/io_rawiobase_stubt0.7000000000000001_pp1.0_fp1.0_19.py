import io
class File(io.RawIOBase):

    def __init__(s, filename, mode="r"):
        s.__f = io.open(filename, mode)
        s.__w = 0

    def write(s, b):
        s.__w = 1
        s.__f.write(b)

    def read(s, *args):
        s.__w = 0
        return s.__f.read(*args)

    def close(s):
        s.__f.close()

    def __getattr__(s, name):
        if s.__w:
            return getattr(s.__f, name)
        raise AttributeError("Not in reading mode")
</code>

