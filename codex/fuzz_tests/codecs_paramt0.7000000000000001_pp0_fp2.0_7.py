import codecs
codecs.register_error('surrogate_or_special', surrogates.SurrogateOrSpecialHandler())

class StringUtil:
    @staticmethod
    def unescape(s):
        return re.sub(r'&(#?)(\w+?);', StringUtil.__unescape_entity, s)

    @staticmethod
    def __unescape_entity(m):
        entity = m.group(2)
        if m.group(1) == '#':
            return chr(int(entity))
        elif entity in name2codepoint:
            return chr(name2codepoint[entity])
        else:
            return m.group(0)

    @staticmethod
    def convert2utf8(s, encoding):
        if encoding == None:
            encoding = 'utf-8'
        if isinstance(s, str):
            return s
        elif isinstance(s, bytes):
            return s.decode(encoding, 'surrogate_or_special')
        else:
            return str(s)

    @staticmethod
    def
