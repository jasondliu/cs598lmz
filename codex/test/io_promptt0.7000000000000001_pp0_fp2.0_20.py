import io
# Test io.RawIOBase 
# Test io.BufferedIOBase

# Test io.RawIOBase
raw_io = io.RawIOBase()
# raw_io.read()  # TypeError: abstract method read() is not implemented
# raw_io.readall() # TypeError: abstract method readall() is not implemented

# Test io.BufferedIOBase
buf_io = io.BufferedIOBase()
# buf_io.read() # TypeError: abstract method read() is not implemented
# buf_io.readall() # TypeError: abstract method readall() is not implemented
# buf_io.readinto() # TypeError: abstract method readinto() is not implemented
# buf_io.readinto1() # TypeError: abstract method readinto1() is not implemented
# buf_io.read1() # TypeError: abstract method read1() is not implemented

# Test io.StringIO
string_io = io.StringIO()
# string_io.write(b'abc') # TypeError: write() argument must be str, not bytes
string_io.write('abc')
# string_io
