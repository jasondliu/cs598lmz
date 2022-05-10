import lzma
# Test LZMADecompressor to see if the input matches the output,
# with extra checks that the state is correctly tracked
def test(input):
    c = lzma.LZMADecompressor()
    buf = []
    while True:
        data = c.decompress(input)
        if data:
            buf.append(data)
        if c.eof:
            break
        #if not data:
        #    raise EOFError
    #print(c.unused_data)
    output = b''.join(buf)
    assert output == c.unused_data + input
    # check against list of buffers
    assert [data for (data, consumed) in c.decompress(b'', True)] == buf
    return len(buf)

# Simple all in one
def test_simple():
    input = b'abcd' * 100000
    assert test(input) == 1

# In chunks
def test_more():
    input = b'x' * 100 + b'abcd' * 100 + b'x' * 100
    test(b'x'
