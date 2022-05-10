import io
# Test io.RawIOBase.readall()

# Test a buffer that is smaller than the raw file size
with io.open("io_readall_file.txt", "rb") as f:
    assert f.readall() == b"aaa"
