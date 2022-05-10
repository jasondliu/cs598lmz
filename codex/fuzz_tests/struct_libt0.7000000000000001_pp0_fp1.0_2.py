import _struct

# from https://docs.python.org/3/library/struct.html
def iter_unpack(format, buffer):
    size = struct.calcsize(format)
    for offset in range(0, len(buffer), size):
        yield struct.unpack_from(format, buffer, offset)

def unpack_file(filename):
    with open(filename, "rb") as f:
        return struct.unpack(">4sx4x4x4x", f.read())

def unpack_file_gen(filename):
    with open(filename, "rb") as f:
        yield from iter_unpack(">4sx4x4x4x", f.read())

def unpack_file_fast(filename):
    with open(filename, "rb") as f:
        buffer = f.read()
    return _struct.iter_unpack(">4sx4x4x4x", buffer)

def unpack_file_fast_gen(filename):
    with open(filename, "rb") as f:
        yield
