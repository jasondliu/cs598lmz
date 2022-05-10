import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

struct.pack("B", b"\x00") # Should not segfault (GH-13099)


# Issue #8497: check that writing an invalid double to StringIO
# doesn't crash Python
try:
    import _testcapi
except ImportError:
    pass
else:
    _testcapi.write_invalid_double_to_stringio(s)
    try:
        s.getvalue()
    except ValueError:
        pass
    else:
        print("expected TypeError")


# Issue #8889: check that using the `-U` command line argument
# doesn't crash Python.
import sys, tempfile

if sys.version_info[0] == 2:
   opt_U = "U"
else:
   opt_U = "B"
try:
    with tempfile.TemporaryFile("r+") as f1:
        f1.write("abc")
        f1.seek(0)
        f2 = open("f2.txt", "w+" + opt_U)
        f2.
