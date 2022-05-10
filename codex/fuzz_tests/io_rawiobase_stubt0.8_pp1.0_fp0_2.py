import io
class File(io.RawIOBase):
   def write(self, data):
      print("Not implemented")

# An object of type File can be used anywhere an object of type RawIOBase is expected
def process(stream):
   print("Not implemented")
process(File())
