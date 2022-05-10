import io
# Test io.RawIOBase
assert isinstance(io.RawIOBase(), io.IOBase)
# Test io.BufferedIOBase
assert isinstance(io.BufferedIOBase(), io.IOBase)
# Test io.TextIOBase
assert isinstance(io.TextIOBase(), io.IOBase)


# Test str.format()

# Test str.format() with precision
assert '{:.2f}'.format(2.1) == '2.10'
assert '{:.2f}'.format(2.12345) == '2.12'
# Test str.format() with alignment
assert '{:>5}'.format(2) == '    2'
# Test str.format() with alignment and precision
assert '{:>8.2f}'.format(2.12345) == '    2.12'
# Test str.format() with alignment, precision, and sign
assert '{:>8.2f}'.format(-2.12345) == '   -2.12'
# Test str.format() with alignment, precision, sign, and base
