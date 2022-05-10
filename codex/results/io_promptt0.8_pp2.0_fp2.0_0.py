import io
# Test io.RawIOBase implementation on Windows
try:
    import _winapi
except ImportError:
    pass
else:
    with _winapi.Pipes('rb', 'wb', False) as (reader, writer):
        if not isinstance(reader, io.RawIOBase) or not isinstance(writer,
            io.RawIOBase):
            raise test.test_support.TestFailed("io.RawIOBase implementation"
                " broken on Windows")
            if test.test_support.verbose:
                print("io.RawIOBase implementation on Windows looks good.")

# Test various io.TextIOBase implementations and their
# io.BufferedRWPair and io.BufferedRandom children.
# Note that "io" is imported as a side effect of import test.support.
with open(test.test_support.TESTFN, "w") as f:
    f.write("ABC\n")
    f.write("DEF\n")
    f.write("abc\n")
    f.write("def\n")
    f.flush()
test_lines = [b"ABC\
