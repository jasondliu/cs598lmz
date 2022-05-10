import io
# Test io.RawIOBase inheritance.
def test_rawiobase():

    class MissingRawIOBase(object):
        pass


# Test io.BufferedIOBase inheritance.
def test_bufferediobase():

    class MissingBufferedIOBase(object):
        pass


# Test io.TextIOBase inheritance.
def test_textiobase():

    class MissingTextIOBase(object):
        pass


