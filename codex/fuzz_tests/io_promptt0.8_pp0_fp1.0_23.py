import io
# Test io.RawIOBase
def test_rawiobase(space):
    io.RawIOBase().read("")
    space.raises_w(space.w_NotImplementedError, io.RawIOBase().readinto, "")
    space.raises_w(space.w_NotImplementedError, io.RawIOBase().readline)
    space.raises_w(space.w_NotImplementedError, io.RawIOBase().readlines)
    space.raises_w(space.w_NotImplementedError, io.RawIOBase().seek, 0)
    space.raises_w(space.w_NotImplementedError, io.RawIOBase().tell)
    space.raises_w(space.w_NotImplementedError, io.RawIOBase().write, "")
    space.raises_w(space.w_NotImplementedError, io.RawIOBase().writelines, [])
    space.raises_w(space.w_NotImplementedError, io.RawIOBase().fileno)
    space.
