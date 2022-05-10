from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd4\xbe\x00\x00(\x007')

# io.BufferedIoBase.readinto() and io.BufferedIoBase.readinto1() are now
# available on various StreamReader and StreamWriter instances.
fp = io.BytesIO(b"\x00\x01\x02\x03")
buf = bytearray(2)
fp.readinto1(buf)
print(buf)
buf = bytearray(2)
fp.readinto(buf)
print(buf)

# sys.warnoptions now always contains a list of strings.
warnings.simplefilter('error')
sys.warnoptions.append('ignore')
warnings.warn('foo')

# typing.Collection(Sized) and typing.Sized(Collection).
class _Test:
    def __len__(self):
        return 0

class _DerivedTest(_Test):
    pass

class _Unrelated:
    pass

assert issubclass(collections.KeysView, collections.abc.Collection)

