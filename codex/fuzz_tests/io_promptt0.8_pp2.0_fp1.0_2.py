import io
# Test io.RawIOBase.readinto()
import array
test_data = array.array('B', 'input data')

class TestRawIO(io.RawIOBase):
    """This class defines an interface compatible with StringIO, but
    instead of storing the input in a String, a BytesIO or other
    file-like object is used to store the input.
    """
    def __init__(self, input_file=None):
        if input_file is None:
            input_file = io.BytesIO()
        self.input_file = input_file
    def write(self, s):
        return self.input_file.write(s)
    def read(self, n=None):
        return self.input_file.read(n)
    def readline(self, length=None):
        return self.input_file.readline(length)
    def seek(self, pos, mode=0):
        return self.input_file.seek(pos, mode)
    def tell(self):
        return self.input_file.tell()
    def truncate(self, pos
