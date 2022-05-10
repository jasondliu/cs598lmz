import lzma
# Test LZMADecompressor

def test2():

    class DummyFile:

        def __init__(self, text, eof=True):
            self.text = text
            self.eof = eof
            self.closed = False

        def read(self, size=-1):
            if self.eof:
                res=self.text
            else:
                res=self.text[:size]
                self.text=self.text[size:]
            return res

        def close(self):
            self.closed = True

        def reset(self):
            if not self.closed:
                self.text = ''
            else:
                self.closed = False

    failures = 0
    # Some hardcoded test data
    data = (b'YUI\xc4\xaa\xc4\xaa\xc4\xaa\xc4\xaa',
            b'YUI\xc4\xaa\xc4\xaa\xc4\xaa\xc4\xaa',
            b'YUI\xc4\xaa\xc4\xaaXUI\xc
