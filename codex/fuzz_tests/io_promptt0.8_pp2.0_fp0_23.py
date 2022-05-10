import io
# Test io.RawIOBase
# Test "ab+"
f = io.open('data/rawiobase.dat', 'ab+', buffering=0)
f.write("0123456789")
f.seek(-5, os.SEEK_CUR)
f.write("abcde")
f.seek(5, os.SEEK_SET)
assert f.read(5) == "56789"
f.seek(0, os.SEEK_END)
assert f.tell() == 10
f.close()

# Test "r+"
f = io.open('data/rawiobase.dat', 'r+', buffering=0)
assert f.read(5) == "01234"
f.seek(-3, os.SEEK_CUR)
f.write("ABC")
assert f.read(1) == "E"
f.close()

# Test "w+"
f = io.open('data/rawiobase.dat', 'w+', buffering=0)
f.write("abc")
f.seek(0, os.
