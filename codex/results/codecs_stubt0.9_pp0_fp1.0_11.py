import codecs

def add_one_codepoint(exc):
    return ("a", exc.start)

def add_utf16_bytes(exc):
    return (b'ab', exc.start)

def add_utf32_bytes(exc):
    return (b'abcd', exc.start)

codecs.register_error("add_one_codepoint", add_one_codepoint)
codecs.register_error("add_utf16_bytes", add_utf16_bytes)
codecs.register_error("add_utf32_bytes", add_utf32_bytes)

SRC = b'ab\xed'

try:
    from pkgutil import find_loader
    found = find_loader('charmapcodec')
except:
    import pkgutil
    import imp
    for _imp, name, _ in pkgutil.iter_importers("codecs"):
        if name == "charmapcodec":
            found = True
            break
    else:
        found = False

if len(sys.argv) > 1:
    verbose = sys.argv[1] == '-v'
else:
    verbose = False


class Test_CharmapCodec(unittest.TestCase):
    pass


##############################################################################
#  Encodings

charmap_encoding_map = {
    "utf-16": "utf_16_le",
    "utf-16-be": "utf_16_be",
    "utf-16-le": "utf_16_le",
    "utf-32": "utf_32_le",
    "
