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

class BOM_Test:
    def __init__(self, enc, bom, s, u, s_bom, u_bom):
        self.enc = enc
        self.bom = bom
        self.s = s
        self.u = u
        self.s_bom = s_bom
        self.u_bom = u_bom
        self.BOM_Test(enc)

    def BOM_Test(self, enc):
        """
        Verify the byte order mark (BOM).

        Written by Mark Hammond to test behaviour of BOM in an email
        to Python-Dev.
        """
        u = self.u
        s = self.s
        bom = self.bom
        s_bom = self.s_bom

        try:
            self.assertEqual(bom.decode(enc), u)
        except UnicodeDecodeError:
            pass

        try:
            self.assertEqual(bom.decode(enc, 'strict'), u)
        except UnicodeDecodeError:

