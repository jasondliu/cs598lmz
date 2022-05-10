import io
# Test io.RawIOBase
class CustomRawIO(io.RawIOBase):

    def read(self, size=-1):
        ...


# Test io.BufferedIOBase
class CustomBufferedIO(io.BufferedIOBase):

    def read(self, size=-1):
        ...


# Test io.TextIOBase
class CustomTextIO(io.TextIOBase):

    def read(self, size=-1):
        ...


# Test io.StringIO
class CustomStringIO(io.StringIO):
    ...


# Test io.BytesIO
class CustomBytesIO(io.BytesIO):
    ...


# Test picklability of io objects
def pickle_io():
    f_name = os.path.join(os.path.dirname(__file__), 'somefile.txt')
    with open(f_name, 'rb+') as f_rb_plus, open(f_name, 'r+b') as f_r_plus_b, open(
        f_name, 'rb') as f_rb, open(f_name, 'r+')
