import io
# Test io.RawIOBase
# Issue #3465: file.readline() doesn't return data after file.seek()
testfile = open(TESTFN, 'wb')
try:
    # 0 bytes
    testfile.write(b'')
    testfile.seek(0)
    s = testfile.readline()
    if s != b'':
        raise TestFailed('empty file.readline() is not the empty string')
    # 1 byte
    testfile.write(b'x')
    testfile.seek(0)
    s = testfile.readline()
    if s != b'x':
        raise TestFailed('file.readline() not single character')
    # 2 bytes
    testfile.write(b'xy')
    testfile.seek(0)
    s = testfile.readline(1)
    if s != b'x':
        raise TestFailed('file.readline(1) not first character')
    # Test seek detection in io.IOBase.read()
    testfile.seek(0)
    s = testfile.read(1
