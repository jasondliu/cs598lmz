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

class TestCodecsMisc(unittest.TestCase):

    @classmethod
    def make_boms(cls, mode, bom_class):
        return (
                (0, bom_class),
                (1, mode.decode('utf-8', "surrogateescape")),
                (2, u'\uFFFE'),
                (3, mode.encode('utf-16', "surrogateescape")),
                )

    @classmethod
    def make_utf16_bad_boms(cls):
        from test.support import bigaddrspacetest
        bom_class = codecs.BOM_UTF16

        # b'\x00'\xfe\xff', b'\xff'\xfe\x00', b'\x00'\xfe\x00', b'\xff'\xfe\xff'
        bad_boms = (
            (b'\x00\xfe\x00', 0xfe),
            (b'\xff\xfe\xff', 0xff),
        )

       
