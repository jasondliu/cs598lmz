import bz2
# Test BZ2Decompressor separately. For some files it doesn't initialize until
# the first chunk of data is fed in.

inp = bz2.BZ2File(testdatafile("sample1.bz2"), "rb")
while True:
    chunk = inp.read(8192)
    if not chunk:
        break
    out = [inp.decompress(chunk)]
    while 1:
        try:
            out.append(inp.decompress())
        except EOFError:
            break
    result = b"".join(out)
    assert_equal(result, SAMPLE_TEXT)

# Try open with 'a' mode.

try:
    f = bz2.BZ2File("xxxx", "a")
except TypeError:
    pass
else:
    f.write("foo")
    f.close()
    assert_equal(open("xxxx", "rb").read(), b"foo")
    os.remove("xxxx")

# Test for issue #10848: passing a file-like object to BZ2File.

from io
