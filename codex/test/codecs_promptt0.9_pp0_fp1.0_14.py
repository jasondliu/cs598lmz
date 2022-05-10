import codecs
# Test codecs.register_error for issue:
# http://bugs.python.org/issue3377

def illegal_error(exc):
    raise UnicodeDecodeError(exc.encoding,
                             exc.object, exc.start, exc.end,
                             'ILLEGAL')

for name in ('latin-1', 'iso8859-1', 'iso-8859-1', 'iso-latin-1',
             '885-9', 'latin-9', 'iso-8859-9', 'latin1', 'oi'):
    codecs.register_error(name, illegal_error)

def errorhandler(dontcare):
    raise UnicodeError("A standard error")

for name in ('ascii', '646', 'iso-8859-10', 'iso_646.irv:1991'):
    codecs.register_error(name, errorhandler)

