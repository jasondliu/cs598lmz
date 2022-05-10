import io
# Test io.RawIOBase.readinto

class BytesIO(io.BytesIO):
    def readinto(self, b):
        return super().readinto(b)

# test readinto with a bytearray
def bytesarray(b):
    return bytearray(b)

def bytesarray_resize(b):
    return bytearray(len(b))

# test readinto with a memoryview
def memview(b):
    return memoryview(b)
def memview_resize(b):
    return memoryview(bytesarray(b))

# test readinto with a writeable buffer
def buffer(b):
    return bytes(b)

# test readinto with a writable array
def array(b):
    return array("B", b)

# test readinto with a writable array
def array_resize(b):
    return array("B", b)

# test readinto with a writable array
def array_fromlist(b):
    return array("B", list(b))

# test readinto with a writable array

