import io
# Test io.RawIOBase
assert issubclass(io.RawIOBase, io.IOBase)
# help(io.RawIOBase)

# Test io.TextIOBase
assert issubclass(io.TextIOBase, io.IOBase)
# help(io.TextIOBase)

# TextIOBaseとRawIOBaseで同じメソッドがあるという擬似静的契約
