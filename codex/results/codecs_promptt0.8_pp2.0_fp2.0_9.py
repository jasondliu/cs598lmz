import codecs
# Test codecs.register_error()
with codecs.open('data/unicode.txt', encoding='utf-16le') as f:
    text = f.read()
    # Let's pretend we misread UTF-16LE as ASCII.
    import unicodedata
    text_as_ascii = text.encode('ascii', 'replace')
    print(text_as_ascii.decode('ascii'))
    # Let's try to fix that by registering a handler for it.
    def correct_decode(text):
        return text.decode('utf-16le', 'replace')
    codecs.register_error('ascii', correct_decode)
    text_as_ascii = text.encode('ascii', 'ascii')
    print(text_as_ascii.decode('ascii'))
