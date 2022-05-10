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

class IncrementalEndecoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        if final:
            return (codecs.BOM_UTF8 + input.encode('utf8'), len(input))
        else:
            return ('', 0)

    def reset(self):
        pass

    def getstate(self):
        return (0, 0)
    def setstate(self, state):
        pass

class IncrementalDecoder(codecs.BufferedIncrementalDecoder):
    _buffer_decode = codecs.utf_8_decode
    def _buffer_encode(self, obj, errors='strict'):
        return (obj, len(obj))

class StreamWriter(codecs.StreamWriter):
    def reset(self):
        pass

class StreamReader(codecs.StreamReader):
    def reset(self):
        pass

def getregentry():
    return codecs.CodecInfo(
        name='utf8-variants',
        encode=lambda
