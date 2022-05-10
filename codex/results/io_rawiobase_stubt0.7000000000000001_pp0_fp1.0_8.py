import io
class File(io.RawIOBase):
  def __init__(self, *args, **kwargs):
    print("File.__init__", args, kwargs)
    io.RawIOBase.__init__(self)
  def read(self, *args, **kwargs):
    print("File.read", args, kwargs)
    return 'foo'
  def write(self, *args, **kwargs):
    print("File.write", args, kwargs)

class FilePath(str):
  def __new__(cls, *args, **kwargs):
    print("FilePath.__new__", cls, args, kwargs)
    return super(FilePath, cls).__new__(cls, "foo")

# This works, because we don't call __new__ on the type, but rather on the
# instance.
foo = FilePath()

# This does not work, because 
foo = FilePath.__new__(FilePath)

# This works, because __new__ is defined on FilePath.__new__, not on
# object.__
