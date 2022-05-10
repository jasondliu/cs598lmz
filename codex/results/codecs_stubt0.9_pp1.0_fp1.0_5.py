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

text = u"¿Qué pasa en el mundo de los charsets?"
print(u"texto original: " + text)
utf8_text = text.encode("utf-8", 'ignore')
print(u"utf-8: " + '?'.join(list(str(utf8_text))).replace('\\x', ''))

gb2312_text = text.encode("gb2312", 'replace')
print(u"gb2312: " + '?'.join(list(str(gb2312_text))).replace('\\x', ''))
mixed = gb2312_text.decode("utf-8",'add_one_codepoint')
print(u"utf-8 malinterpretado: " + mixed)
mixed = mixed.encode('utf-16', 'add_utf16_bytes')
print(u"utf-16 malinterpretado: " + mixed)
mixed = mixed.decode('utf-32', 'add_utf32_bytes')
print(u"utf-32 malinterpretado: " + mixed
