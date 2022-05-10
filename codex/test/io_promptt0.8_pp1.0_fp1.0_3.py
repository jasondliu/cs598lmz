import io
# Test io.RawIOBase to see if it's a file-like object with a "write" function.
# If it is, then the resulting object is a true file object.
# Otherwise, it's a StringIO object, and we pass it to StringIO's constructor.
#
# This is slightly gross, but not as gross as our original implementation which
# used the "file" builtin to check if it was a file-like object. The problem was
# that file is only available on Python 2, and if you run under 3.2, it's not
# available. In Python 3.2, the "file" type was removed, and the "io" module
# became the standard way of dealing with files. This is hopefully the easiest
# way to get the best of both worlds.
def load_as_file_or_stringio(filename):
    if isinstance(filename, io.RawIOBase):
        if hasattr(filename, 'write'):
            return filename
        else:
            return io.StringIO(filename.read())
    else:
        return open(filename, 'r')

