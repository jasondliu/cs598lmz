import io
# Test io.RawIOBase
        rio = io.RawIOBase()
# Test io.BufferedIOBase
        ibio = io.BufferedIOBase()
# Test io.TextIOBase
        tio = io.TextIOBase()
# Test io.FileIO
        fio = io.FileIO()
# Test io.BytesIO
        bio = io.BytesIO()
# Test io.StringIO
        sio = io.StringIO()
# Test io.BufferedReader
        br = io.BufferedReader()
# Test io.BufferedWriter
        bw = io.BufferedWriter()
# Test io.BufferedRWPair
        rwp = io.BufferedRWPair()
# Test io.BufferedRandom
        brand = io.BufferedRandom()
# Test io.TextIOWrapper
        tiw = io.TextIOWrapper()
# Test io.TextIOWrapper(errors='strict')
        tiwe = io.TextIOWrapper(errors='strict')

    def test_io_tools(self):
# Test io.raw_
