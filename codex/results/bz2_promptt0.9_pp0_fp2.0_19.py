import bz2
# Test BZ2Decompressor.__nonzero__(), need to export internal state.
D = bz2.BZ2Decompressor()
D.__nonzero__()

D.needs_input = False
D.expand("")

D.needs_input = False
D.decompress("")
# Failed due to a bug, but provides a handy consistency test.
D = bz2.BZ2Decompressor(100)
# Needs initialisation to work.
def go(data):
    D.decompress(data)
    D.flush()
    return D.unused_data
assert bz2.decompress(bz2.compress(b'x')) == b'x'
assert go(bz2.compress(b'x') + b'z') == b'z'
assert go(bz2.compress(b'x')[:1] + b'z') == bz2.compress(b'x')[:1] + b'z'
# Test the BZ2File compression state machine.
# The bug was that one state was mis
