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

def test_main():

    def test(encoding, indata, decattr, decsep,
             decfunc, decargs, decrj, encattr, encsep,
             encfunc, encargs, enclj, enclv, enclo):
        decinfo = (decattr, decsep, decfunc, decargs, decrj)
        encinfo = (encattr, encsep, encfunc, encargs, enclj, enclv, enclo)
        print(repr(indata))
        d, size = codecs.getdecoder(encoding)
        enc, size = codecs.getencoder(encoding)
        got = d(indata, errors='add_one_codepoint')[0]
        if decinfo != got:
            raise error, 'encoding=%s: expected %r, got %r' % (encoding, decinfo, got)
        got = d(indata, errors='surrogatepass')[0]
        if decinfo != got:
            raise error, 'encoding=%s: expected %
