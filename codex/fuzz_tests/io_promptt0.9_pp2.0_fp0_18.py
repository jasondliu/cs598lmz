import io
# Test io.RawIOBase
for bufsize in (0, 1, 2, 118, 119, 120, 121, 698, 699, 700):
    io.RawIOBase._test_wrap(io.RawIOBase(), bufsize=bufsize)
    io.RawIOBase._test_unwrap(io.RawIOBase(), bufsize=bufsize)
from _io import UnsupportedOperation
# Test io.BufferedIOBase
for bufsize in (0, 1, 2, 118, 119, 120, 121, 698, 699, 700):
    io.BufferedIOBase._test_wrap(io.BufferedIOBase(), bufsize=bufsize)
    io.BufferedIOBase._test_unwrap(io.BufferedIOBase(), bufsize=bufsize)
# Test seek
for class_ in (io.BufferedReader, io.BufferedWriter, io.BufferedRWPair, io.BufferedRandom):

    class ClassWithSeek(class_):

        def seekable(self):
            return True
    ClassWithSeek._test_seek(ClassWithSeek(), bufsize=400)


