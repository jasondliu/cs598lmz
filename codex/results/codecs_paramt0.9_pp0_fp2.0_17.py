import codecs
codecs.register_error('special', special)

def iter_lines_with_failover(source, codec=None, encoding=None, errors='strict'):
    if hasattr(source, 'readline'):
        return iter(source.readline, '')
    else:
        def decode_line(line):
            if codec is not None:
                return codec(line)[0]
            if encoding is not None:
                return line.decode(encoding, errors)
            return line
        return itertools.imap(decode_line, source)

def encode_output(text, encoding, errors):
    """Byteify `text` using `encoding` and `errors` (strict, replace,
    surrogateescape, special)."""
    assert errors in ('strict', 'replace', 'surrogateescape', 'special')
    if six.PY3:
        if encoding.lower() != locale.getpreferredencoding().lower():
            return text.encode(encoding, errors)
        else:
            return text
    else:
        if encoding.lower() == locale
