import io
# Test io.RawIOBase in read-mode
import io
with io.RawIOBase() as infile:
    infile.read()
# Test io.RawIOBase in write-mode
import io
with io.RawIOBase() as outfile:
    outfile.write(b'')
# Test io.TextIOBase in read-mode
import io
with io.TextIOBase() as infile:
    infile.read()
# Test io.TextIOBase in write-mode
import io
with io.TextIOBase() as outfile:
    outfile.write(u'')

# Test compatibility with profilehooks' line_profiler
# http://packages.python.org/line_profiler/
try:
    from line_profiler import LineProfiler
except ImportError:
    pass
else:
    @LineProfiler
    def foo():
        with open("/dev/null", "a") as out:
            out.write("xxx")

# Test that closing a file with weakrefs to its IO objects doesn't
# segfault
try:
    import _test
