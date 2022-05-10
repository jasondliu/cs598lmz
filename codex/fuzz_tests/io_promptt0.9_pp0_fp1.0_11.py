import io
# Test io.RawIOBase as outputstream
outputstream = io.BytesIO()

# try to instantiate the class as functor
test_instance = outputstream()

assert outputstream() is not None
