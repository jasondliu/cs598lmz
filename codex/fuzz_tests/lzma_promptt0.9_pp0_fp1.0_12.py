import lzma
# Test LZMADecompressor errors by feeding 'corrupt' data with differing sizes
# and checking that LZMAError is raised.
with lzma.open(TESTFN, 'wb') as fp:
    fp.write(b'foobar')
    fp.close()
with open(TESTFN, 'rb') as f:
    comp = lzma.LZMADecompressor()
    f.seek(3)
    try:
        comp.decompress(f.read(1))
    except lzma.LZMAError:
        pass
    else:
        self.fail("LZMAError not raised")
    try:
        comp.decompress(b'maybe')
    except lzma.LZMAError:
        pass
    else:
        self.fail("LZMAError not raised")
    try:
        comp.decompress(b'lastchance')
    except lzma.LZMAError:
        pass
    else:
        self.fail("LZMAError not raised")
shutil.unlink(TEST
