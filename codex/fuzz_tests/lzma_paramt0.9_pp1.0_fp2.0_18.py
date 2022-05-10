from lzma import LZMADecompressor
LZMADecompressor

# reading the bytes
with open('../Downloads/snapshot_pages.htm.xz', 'rb') as fh:
    obj = LZMADecompressor()
    fh.seek(0, 2)
    s = obj.decompress(fh.read())
    print(len(s))

# with the new file, this should get the files
with open('../Downloads/snapshot_pages.htm.xz', 'rb') as fh:
    obj = LZMADecompressor()
    fh.seek(0, 2)
    header = fh.read(4)
    s = obj.decompress(fh.read())
    print(s)
</code>
So it does seem to be some bug in the macOS <code>xz</code> package, though maybe more likely that it is a feature not supported in <code>lzma</code>.
To be clear, the <code>xz</code> package installed on macOS is from Apple which has the version string "5.2.3 (Apple Inc. build 5666
